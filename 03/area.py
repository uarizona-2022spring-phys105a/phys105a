#!/usr/bin/env python3



def area(r):
    return ______

import argparse

parser = argparse.ArgumentParser(description="""
This program takes exactly one argument from the command line,
interpret it as the radius of a circle, and then compute and print out
the area of the circle.
""")

parser.add_argument("r", type=float, help="the radius of a circle")

args = parser.parse_args()

r = args.r

print("Compute the area of a circle with radius", r, " using the equation A = pi r^2.")

#A = area(r)
#print("A =", A)
