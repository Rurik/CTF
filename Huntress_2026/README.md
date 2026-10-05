# Huntress CTF 2026 client

This folder contains two files: `huntress.py` and this README. The script lists
Game Master challenges, starts or resumes attempts, downloads assigned artifacts,
checks status, and submits your answers using your own account. Solve the
challenges yourself; no challenge answers or solvers are included.

## 1. Install

Use Python **3.10 or newer**. Open a terminal in the folder containing
`huntress.py`. These commands use bash/zsh on macOS, Linux, or Homebase:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install 'requests>=2.32.3,<3'
```

In a new terminal, return to this folder and activate `.venv` again.

## 2. Connect with your own account

Choose either Homebase or your own computer.

### Inside your Homebase terminal

CourseStack supplies your identity through its internal proxy. Clear any direct
connection settings and list challenges:

```bash
unset HUNTRESS_API_URL HUNTRESS_AUTH_HEADER HUNTRESS_AUTH_VALUE
python huntress.py list --all
```

### On your own computer

First, run this **once in your own Homebase terminal** to save your pairing token:

```bash
umask 077
curl --fail --silent --show-error -X POST \
  'http://10.0.0.219/huntress-ctf-proxy?op=pair' \
  -o "$HOME/gm-pairing.json"
```

If you already paired, use the pairing file you saved earlier. Pairing does not
return the token again. Transfer that file privately to your own computer and
save it as `~/gm-pairing.json`.

In your local terminal, with `.venv` activated:

```bash
chmod 600 "$HOME/gm-pairing.json"
export HUNTRESS_API_URL='https://2026.huntress.ctf.games'
export HUNTRESS_AUTH_HEADER='Authorization'
export HUNTRESS_AUTH_VALUE="$(python -c 'import json; from pathlib import Path; print("Bearer " + json.loads((Path.home() / "gm-pairing.json").read_text())["token"])')"
python huntress.py list --all
```

Repeat the three `export` commands in each new terminal session. The direct HTTPS
connection uses your pairing token; it does not require a VPN.

## 3. Get a challenge

Replace `your-challenge-id` below with an exact ID returned by `list`.

```bash
python huntress.py start your-challenge-id
python huntress.py artifact your-challenge-id
```

The first command displays the task and saves
`challenges/your-challenge-id/task.json`. Read its questions, answer formats, and
exact `answer_ids`. The second command saves the assigned download as
`challenges/your-challenge-id/artifact.bin`; multiple advertised per-set downloads
are assembled into a ZIP at that same filename.

Single Solve is untimed. Starting a `/time_trial` or `/mastery` challenge can start
its server timer. Use the complete mode-specific ID returned by `list`.

## 4. Submit your answer

After solving your own task, create
`challenges/your-challenge-id/answers.json` with the exact answer IDs from the task
as keys and your answers as strings. For example, the structure is:

```json
{
  "answer-id-from-task": "your-answer"
}
```

Include an entry for each required answer, then submit:

```bash
python huntress.py submit your-challenge-id \
  --answers-file challenges/your-challenge-id/answers.json
```

The response is printed and saved as
`challenges/your-challenge-id/result.json`. Read the server's result to determine
whether it accepted your answers. If it returns a flag, enter that flag in the
corresponding website answer box. The script submits Game Master answers; it does
not fill out the website for you.

## Other useful commands

```bash
python huntress.py list --day 3
python huntress.py list --search warmups
python huntress.py status your-challenge-id
python huntress.py retry your-challenge-id
python huntress.py --help
python huntress.py submit --help
```

`retry` explicitly requests renewal of an expired attempt. After a network error,
check `status` before repeating a start, submit, or retry; the script does not
automatically retry requests. Artifact downloads do not overwrite existing
files; use `artifact your-challenge-id --out artifact-2.bin` to save another copy.

Keep your pairing file and generated `challenges/` folder private: they can
contain account credentials, download capabilities, and flags. To pass this tool
on, send only the original `huntress.py` and `README.md` files.
