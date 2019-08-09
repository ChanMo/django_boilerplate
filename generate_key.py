#!/usr/bin/env/python

import random


def main():
    key = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
    print(key)

if __name__ == '__main__':
    main()
