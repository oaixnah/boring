# coding: utf-8

import sys
import random
import string


def index(count: int = 6, level: int = 1):
    if level < 1 or level > 3:
        raise ValueError("1 < `level` < 3")

    print('New Password: ', ''.join(
        (random.choice(''.join([string.ascii_letters, string.digits, '!@#$%^&*'][:level])) for _ in range(count))))


if __name__ == '__main__':
    _t = sys.argv
    if len(_t) == 3:
        try:
            index(int(_t[1]), int(_t[2]))
        except ValueError:
            raise ValueError('<count> <level> should be `int` .')
    else:
        print('python random_password.py <count> <level>')

