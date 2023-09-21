#! /usr/bin/python2

import time
from copy import copy, deepcopy

# copy is used for 1D tables (without sub tables) !!!
# deepcopy is used for more D (with sub tables)

def main():
    spisek1 = ["Franci", "Peter", "Marusa"]
    spisek2 = spisek1
    
    temp = spisek1.pop(1) # if you change spisek1, spisek2 also changes

    print(temp)
    print(repr(spisek1))
    print(repr(spisek2))

    spisek1.append("Peter")

    print("Spisek 1 po append: " + repr(spisek1))

    spisek3 = copy(spisek1)
    spisek3.pop(0)
    print("Spisek1: " + repr(spisek1))
    print("Spisek3: " + repr(spisek3))




if __name__ == "__main__":
    main()