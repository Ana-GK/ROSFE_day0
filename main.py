#! /usr/bin/python2
# za izvajanje pozeni chmod +x main.py
# ./main.py

"""########################
###Primer dodajanja modulov
########################"""

import time # dodamo modul za nadzor casa
# from time import sleep
# from time import *
# import time as t


def main():
    i = 1.1
    print("Test: %d" %i)
    # print "test" # tudi deluje
    time.sleep(1)
    print("Test"+str(i))

if __name__ == "__main__": # preverimo, če je bil program zagnan kot modul
    main() # klicemo main