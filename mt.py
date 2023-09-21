#! /usr/bin/python2

import time
from threading import Thread
import sys
from multiprocessing import Lock

global thr1running
thr1running = False


def thr1():
    global thr1running, mx
    thr1running = True
    num = 1
    numPrev = 1
    while thr1running:
        mx.acquire()
        temp = num
        num = num + numPrev
        numPrev = temp
        print(num)
        sys.stdout.flush()
        time.sleep(5)
        mx.release()
        time.sleep(0.5)

def thr2():
    while True:
        print("Daemon thread")
        time.sleep(1)

def main():
    global thr1running, mx
    thr1obj = Thread(target=thr1,args=())
    thr1obj.start()

    thr2obj = Thread(target=thr2)
    thr2obj.setDaemon(True)
    thr2obj.start()
    try:
        while True:
            mx.acquire()
            print("Main thread")
            time.sleep(0.5)
            mx.release()
    except KeyboardInterrupt:
            thr1running = False
            print("Cakam na thread")
            thr1obj.join()
            print("Izhod")

if __name__ == "__main__":
    main()