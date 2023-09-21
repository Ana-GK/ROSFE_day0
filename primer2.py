#! /usr/bin/python2

import time
from collections import deque

def main():
    for n in range(10,0,-1):
        print(str(n))
    # ime = raw_input("Vpisi svoje ime: ")
    # print(ime)

    d = deque(maxlen=10)
    d.append("Nekaj")
    for o in range(1,35):
        d.append(str(o))
    print(d)


if __name__ == "__main__":
    main()