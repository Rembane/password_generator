#!/usr/bin/env python2

import random, string, subprocess

def generate_password(length, source):
    return ''.join((random.choice(source) for x in range(length)))

if __name__ == "__main__":
    password = generate_password(25, list(set(string.ascii_letters + string.digits) - set('ioIO10')))

    # Copy password to all clipboards
    for args in ('-pi', '-bi'):
        p = subprocess.Popen(['xsel', args], stdin=subprocess.PIPE)
        p.communicate(password)
