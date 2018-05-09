#!/usr/bin/python
from __future__ import print_function, division
import sys


#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except ValueError:
        print("non-numerical inputs, sorry! no can do!")
        sys.exit(1)

    x1, x2 = find_roots(a, b, c)
    print ("This is x1: %f" %x1)
    print ("This is x2: %f" %x2)


def find_roots(a,b,c):
    try:
        mid = b**2 - 4*a*c
        sqrt_mid = mid**(1/2)
        x1 = (-b + sqrt_mid)/(2*a)
        x2 = (-b - sqrt_mid)/(2*a)
        return x1, x2
    except ValueError:
        print("imaginary roots. sorry dude, no can do!")
        sys.exit(1)
    except ZeroDivisionError:
        print("can't find roots -- your leading coefficient is 0")
        sys.exit(1)
    


    
if __name__=="__main__":
        main()
