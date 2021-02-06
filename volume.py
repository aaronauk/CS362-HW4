import sys
import math

def volume(x):
    if(not isinstance(x, int)):
        print("Your input is not a integer.")
        return -1
    elif (x < 0):
        print("A length of a cube cannot be a negative number.")
        return -1
    x = math.pow(x,3)
    return x

