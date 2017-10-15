import itertools
import subprocess
from threading import Timer

opt = [0, 1]
proc_name = ['/Users/bbaskin/Development/simavr/simavr/run_avr', '-m', 'atmega328p', '--freq', '8000000', 'remorse.ino.hex']


def gen_input():
    print('gen_input')
    input_list = []
    for i in itertools.product(opt, repeat=8):
        input_list += [''.join(map(str, i))]

    return input_list


def check_output(proc, test):
    timer = Timer(1, lambda proc: proc.kill(), [proc])
    try:
        timer.start()
        out, err = proc.communicate('%s\n' % test)
        return out
    finally:
        timer.cancel()
        return ''


if __name__ == '__main__':

    input_list = gen_input()
    for test in input_list:
        print('open proc with %s arg    ' % test)
        proc = subprocess.Popen(proc_name, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = check_output(proc, test)
        if out:
            print('out = %s' % out)

