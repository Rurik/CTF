#!/usr/bin/env python3
"""Huntress Game Master client. Protocol based on the provided API screenshot."""
import argparse
import hashlib
import io
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
import threading
import zipfile
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import requests

PROXY_URL = 'http://10.0.0.219/huntress-ctf-proxy'


class Client:
    def __init__(self, url, headers=None, timeout=20):
        parts = urlsplit(url)
        internal_proxy = (parts.scheme == 'http' and parts.netloc == '10.0.0.219'
                          and parts.path == '/huntress-ctf-proxy')
        if (parts.scheme != 'https' and not internal_proxy) or not parts.netloc or parts.fragment:
            raise ValueError('Use HTTPS or the documented CourseStack internal HTTP proxy.')
        self.url = url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(headers or {})

    def request(self, method='GET', params=None, body=None, binary=False):
        parts = urlsplit(self.url)
        query = dict(parse_qsl(parts.query, keep_blank_values=True))
        query.update(params or {})
        url = urlunsplit(parts._replace(query=urlencode(query)))
        response = self.session.request(method, url, json=body,
                                        timeout=self.timeout, allow_redirects=False)
        # Never retry a POST: a retry could create a new timed attempt.
        if not 200 <= response.status_code < 300:
            raise RuntimeError(f'HTTP {response.status_code}; request stopped. '
                               'Check endpoint/authentication and server state before retrying.')
        if binary:
            return response.content, response.headers.get('Content-Type', '')
        try:
            return response.json()
        except ValueError:
            raise RuntimeError('Expected JSON; check endpoint/authentication.') from None

    def start(self, challenge, extra=None):
        body = dict(extra or {})
        body['challenge'] = challenge
        body['op'] = 'start'
        return self.request('POST', body=body)

    def submit(self, challenge, answers):
        if not isinstance(answers, dict) or not answers or any(not isinstance(v, str) for v in answers.values()):
            raise ValueError('Answers must be a nonempty JSON object with string values.')
        return self.request('POST', body={'op': 'submit', 'challenge': challenge, 'answers': answers})

    def artifact(self, challenge, task=None, workers=8):
        if task and not task.get('download') and task.get('artifacts'):
            entries = task['artifacts']
            if len(entries) > 1:
                return self.artifact_bundle(challenge, task, workers)
            task = entries[0]
        params = {'op': 'artifact', 'challenge': challenge}
        if task and task.get('download'):
            link = urlsplit(task['download'])
            if link.scheme or link.netloc or link.path not in ('', '/') or link.fragment:
                raise ValueError('Unexpected artifact link; only same-service relative downloads are supported.')
            params = dict(parse_qsl(link.query))
            if params.get('op') != 'download':
                raise ValueError('Unexpected artifact download operation.')
        data, content_type = self.request(params=params, binary=True)
        if task and task.get('sha256'):
            if hashlib.sha256(data).hexdigest() != task['sha256'].lower():
                raise ValueError('Artifact SHA-256 does not match the assigned task.')
        return data, content_type

    def artifact_bundle(self, challenge, task, workers):
        entries = task['artifacts']
        questions = task.get('questions', [])
        ids = task.get('answer_ids', [])
        if (len(entries) != len(questions) or [q.get('id') for q in questions] != ids
                or [q.get('set') for q in questions] != list(range(1, len(entries) + 1))):
            raise ValueError('Per-set downloads do not align with the numbered question contract.')
        names = [q.get('artifact') for q in questions]
        if (len(set(names)) != len(names) or any(not isinstance(n, str) or
                not n or '/' in n or '\\' in n or n in ('.', '..') for n in names)):
            raise ValueError('Expected distinct simple artifact filenames in the question contract.')
        if any(not isinstance(e, dict) or not e.get('download') or not e.get('sha256') for e in entries):
            raise ValueError('Each per-set download must supply a link and SHA-256.')
        local = threading.local()
        clones = []
        lock = threading.Lock()
        def fetch(entry):
            # requests Sessions are not shared between concurrent workers.
            if not hasattr(local, 'client'):
                clone = Client(self.url, dict(self.session.headers), self.timeout)
                clone.session.cookies.update(self.session.cookies)
                clone.session.trust_env = self.session.trust_env
                local.client = clone
                with lock:
                    clones.append(clone)
            return local.client.artifact(challenge, entry)[0]
        try:
            with ThreadPoolExecutor(max_workers=min(workers, len(entries))) as pool:
                # map preserves the advertised set order even if requests finish out of order.
                blobs = list(pool.map(fetch, entries))
        finally:
            for clone in clones:
                clone.session.close()
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_STORED) as archive:
            for name, blob in zip(names, blobs):
                archive.writestr(name, blob)
        return buffer.getvalue(), 'application/zip; assembled-from-verified-downloads'


def challenge_dir(challenge):
    parts = challenge.split('/')
    if any(not part or part in ('.', '..') or
           any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_' for c in part)
           for part in parts):
        raise ValueError('Challenge ID contains unsafe path characters.')
    return Path('challenges').joinpath(*parts)


def beneath(folder, name):
    path = folder / name
    if not path.resolve().is_relative_to(Path('challenges').resolve()):
        raise ValueError('Output files must stay beneath ./challenges/. Use a relative output name.')
    return path


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def dump(value):
    print(json.dumps(value, indent=2, ensure_ascii=False))


def read_object(path):
    obj = json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(obj, dict):
        raise ValueError(f'{path} must contain a JSON object.')
    return obj


def field(obj, path):
    for part in path.split('.'):
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj


def load_solver(path):
    path = Path(path).resolve()
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location('ctf_solver', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not callable(getattr(module, 'solve', None)):
        raise ValueError('Solver must define solve(task, artifact).')
    return module


def run(client, args):
    solver = load_solver(args.solver)  # Import/preparation happens before timer.
    if callable(getattr(solver, 'prepare', None)):
        solver.prepare()
    extra = read_object(args.start_json) if args.start_json else None
    expected = json.loads(args.success_value)
    if args.count > 1 and not args.success_path:
        raise ValueError('Repeated attempts require --success-path and --success-value '
                         'from a verified successful server response.')
    root = beneath(challenge_dir(args.challenge), args.out)
    root.mkdir(parents=True, exist_ok=True)
    for index in range(args.count):
        folder = root / f'{time.time_ns()}-{index + 1}'
        folder.mkdir()
        # Conservative local measure includes start-request network latency.
        started = time.perf_counter()
        renewed = None
        if getattr(args, 'retry', False):
            renewed = client.request('POST', body={'op': 'retry', 'challenge': args.challenge})
        # A retry may itself supply a full task; otherwise start/resume it immediately.
        if renewed and (renewed.get('flag') or (renewed.get('questions') and renewed.get('answer_ids'))):
            task = renewed
        else:
            task = client.start(args.challenge, extra)
        if isinstance(task.get('flag'), str) and task['flag']:
            save_json(folder / 'task.json', task)
            save_json(folder / 'result.json', task)
            if renewed is not None:
                save_json(folder / 'retry.json', renewed)
            print('Game Master returned an existing flag; no solve or submission needed.', file=sys.stderr)
            dump(task)
            return
        artifact = None
        try:
            artifact = client.artifact(args.challenge, task, workers=getattr(args, 'workers', 8)) if args.artifact else None
            answers = solver.solve(task, artifact[0] if artifact else None)
            if not isinstance(answers, dict) or not answers:
                raise ValueError('solve() must return a nonempty answer-ID-to-answer dictionary.')
            before_submit = time.perf_counter() - started
            if args.budget and before_submit >= args.budget:
                raise RuntimeError(f'Local budget exhausted before submission ({before_submit:.3f}s). '
                                   'Attempt remains active; inspect status before retrying.')
            result = client.submit(args.challenge, answers)
            elapsed = time.perf_counter() - started
        finally:
            # Disk I/O stays outside the timed path, including on solver failure.
            (folder / 'task.json').write_text(json.dumps(task, indent=2), encoding='utf-8')
            if renewed is not None:
                save_json(folder / 'retry.json', renewed)
            if artifact:
                (folder / 'artifact.bin').write_bytes(artifact[0])
                (folder / 'artifact-content-type.txt').write_text(artifact[1], encoding='utf-8')
        (folder / 'result.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
        print(f'Attempt {index + 1}: {elapsed:.3f}s locally; saved {folder}', file=sys.stderr)
        dump(result)
        # Server result is authoritative; never infer a flag or acceptance field.
        if args.success_path:
            try:
                accepted = field(result, args.success_path) == expected
            except (KeyError, IndexError, TypeError, ValueError):
                accepted = False
            if not accepted:
                raise RuntimeError('Acceptance check failed; stopping before another attempt.')
        if args.budget and elapsed >= args.budget:
            print('Local elapsed time exceeded the budget; check server timing/result.', file=sys.stderr)
            if index + 1 < args.count:
                raise RuntimeError('Stopping repeated attempts after local budget overrun.')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', default=os.environ.get('HUNTRESS_API_URL') or PROXY_URL)
    parser.add_argument('--headers-file', help='JSON object of exact documented auth headers')
    parser.add_argument('--timeout', type=float, default=20)
    commands = parser.add_subparsers(dest='command', required=True)
    listing = commands.add_parser('list')
    listing.add_argument('--day', type=int)
    listing.add_argument('--lane')
    listing.add_argument('--all', action='store_true', help='List every released challenge')
    listing.add_argument('--search', help='Search challenge IDs (2–64 characters)')
    for name in ['start', 'status', 'artifact', 'submit', 'run', 'retry']:
        sub = commands.add_parser(name)
        sub.add_argument('challenge', help='Exact challenge ID from Game Master')
        if name == 'artifact':
            sub.add_argument('--out', default='artifact.bin', help='Relative filename inside this challenge folder')
        if name in ['start', 'run']:
            sub.add_argument('--start-json', help='Additional documented start fields, if any')
        if name == 'submit':
            sub.add_argument('--answers-file', required=True)
        if name == 'run':
            sub.add_argument('--solver', required=True)
            sub.add_argument('--artifact', action='store_true', help='Download artifact inside timed path')
            sub.add_argument('--retry', action='store_true', help='Explicitly renew an expired attempt immediately before solving')
            sub.add_argument('--workers', type=int, default=8, help='Parallel workers for per-set artifact downloads')
            sub.add_argument('--count', type=int, default=1)
            sub.add_argument('--budget', type=float, default=6)
            sub.add_argument('--success-path', help='Verified acceptance field, e.g. result.accepted')
            sub.add_argument('--success-value', default='true', help='Expected value as JSON')
            sub.add_argument('--out', default='runs', help='Relative log folder inside this challenge folder')
    commands.add_parser('pair', help='POST op=pair using authenticated proxy URL/session')
    commands.add_parser('openapi', help='Discover the actual API contract')
    args = parser.parse_args(argv)
    if not args.url:
        parser.error('Set HUNTRESS_API_URL or --url to the actual API endpoint.')
    if args.timeout <= 0:
        parser.error('--timeout must be positive')
    if args.command == 'run' and (args.count < 1 or args.budget < 0):
        parser.error('--count must be positive and --budget nonnegative')
    if args.command == 'run' and args.workers < 1:
        parser.error('--workers must be positive')
    try:
        headers = read_object(args.headers_file) if args.headers_file else {}
        # Exact value, including any required prefix. No assumed token scheme.
        if os.environ.get('HUNTRESS_AUTH_HEADER'):
            headers[os.environ['HUNTRESS_AUTH_HEADER']] = os.environ['HUNTRESS_AUTH_VALUE']
        client = Client(args.url, headers, args.timeout)
        if args.command == 'list':
            params = {'op': 'list'}
            if args.day is not None:
                params['day'] = args.day
            if args.lane is not None:
                params['lane'] = args.lane
            if args.all:
                params['all'] = 'true'
            if args.search is not None:
                params['search'] = args.search
            dump(client.request(params=params))
        elif args.command == 'pair':
            dump(client.request('POST', params={'op': 'pair'}))
        elif args.command == 'openapi':
            dump(client.request(params={'op': 'openapi'}))
        elif args.command == 'retry':
            folder = challenge_dir(args.challenge)
            result = client.request('POST', body={'op': 'retry', 'challenge': args.challenge})
            save_json(folder / 'retry.json', result)
            dump(result)
        elif args.command == 'start':
            folder = challenge_dir(args.challenge)
            task = client.start(args.challenge, read_object(args.start_json) if args.start_json else None)
            save_json(folder / 'task.json', task)
            dump(task)
        elif args.command == 'status':
            folder = challenge_dir(args.challenge)
            result = client.request(params={'op': 'status', 'challenge': args.challenge})
            save_json(folder / 'status.json', result)
            dump(result)
        elif args.command == 'submit':
            folder = challenge_dir(args.challenge)
            result = client.submit(args.challenge, read_object(args.answers_file))
            save_json(folder / 'result.json', result)
            dump(result)
        elif args.command == 'artifact':
            folder = challenge_dir(args.challenge)
            path = beneath(folder, args.out)
            path.parent.mkdir(parents=True, exist_ok=True)
            task_file = folder / 'task.json'
            task = read_object(task_file) if task_file.exists() else None
            data, content_type = client.artifact(args.challenge, task)
            # Avoid silently overwriting locally analyzed files.
            with path.open('xb') as output:
                output.write(data)
            print(f'{path}: {len(data)} bytes ({content_type})')
        elif args.command == 'run':
            run(client, args)
        return 0
    except (OSError, ValueError, RuntimeError, KeyError, requests.RequestException) as exc:
        # Requests exceptions can contain credential-bearing URLs; keep errors sanitized.
        if isinstance(exc, requests.RequestException):
            print('Network request failed; inspect server status before retrying.', file=sys.stderr)
        else:
            print(f'Error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
