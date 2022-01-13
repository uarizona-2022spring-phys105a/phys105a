#!/usr/bin/env python3

#------------------------------------------------------------------------------
# There are some sample python codes

# In python, lines start with "#" are comments and are not executed.
# You may use comments to clarify your program.

#------------------------------------------------------------------------------
# To assign a numerical value to a python variable, simply:
a = 10

# In python, you may use the print function to print a variable.
print('print', a)

#------------------------------------------------------------------------------
# It is straightforward to do math in python.
print(a + 3)
print(a - 3)
print(a * 3)

# Power uses two stars, i.e., "**"
print(a**3)

#------------------------------------------------------------------------------
# Divsion is trick... in python3, a "single" division sign is floating
# point division
print(a/3)

# But double-division is integer division
print(a//3)

#------------------------------------------------------------------------------
# The integer division is logically equivalent to applying a floor
# function to the floating point division.
# However, the floor function is not a default (built-in) function.
# You need to import it from the math package:

from math import floor

print(floor(a/3))

#------------------------------------------------------------------------------
# There are many useful functions and constants in the math package:

from math import pi, sin, cos

print(pi)
print(sin(pi))
print(cos(pi))
