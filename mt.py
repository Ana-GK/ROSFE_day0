#! /usr/bin/python2

import time
from threading import Thread
import sys

global thr1running
thr1running = False

def thr1():
    global thr1running
    thr1running = True
    num = 1
    numPrev = 1
    while thr1running:
        temp = num
        num = num + numPrev
        numPrev = temp
        print(num)
        sys.stdout.flush()
        time.sleep(5)

def main():
    global thr1running
    thr1obj = Thread(target=thr1,args=())
    thr1obj.start()
    try:
        while True:
            print("Main thread")
            time.sleep(0.5)
    except KeyboardInterrupt:
            thr1running = False
            print("Cakam na thread")
            thr1obj.join()
            print("Izhod")

if __name__ == "__main__":
    main()