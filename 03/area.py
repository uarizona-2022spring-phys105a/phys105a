#!/usr/bin/env python3
#
# 0. INTRODUCTION
#
# In this hands-on, we will introduce how to write a python script
# that runs like a program on *nix systems.  This program `area.py`
# would take exactly one argument from the command line, interpret it
# as the radius of a circle, and then compute and print out the area
# of the circle.
#
# For most part, you just need to follow the instruction to uncomment
# codes.  And even for the places that you need to program, all you
# need is some basic statements that we covered in the hands-on
# section:
#
#    https://github.com/uarizona-2022spring-phys105a/phys105a/blob/main/03/Handson.ipynb
#
# Please look for "TODO:" for the places that you are supposed to make
# change.
#
# Note, however, in order to explain how this script works, we need to
# jump to different parts of the code non-linearly.  To make it easier
# to find the code, we use a long line of `#====...====` to indicate
# these different "code sections".
#
# By the way, in interpreted language, there's no real difference
# between `program` and `script`.  So we will use these two terms
# interchangeablely in this file.
#
# To start, let's go to THE END of this script and look for
# "1. MAIN SECTION".
#
#==============================================================================
# 2. AREA SOLVER
#
# NOTE: please read section "1. MAIN SECTION" before you read this section.
#
# Here, we want to program a function that solve the area of a circle.
# However, because the constant `pi` is a keyword of the python
# language, you need to bring it in from the math library.
#
# TODO: write a statement to import `pi` from the math library
#


# Next, we can define a function area() that takes in the radius and
# return the area.
#
# TODO: type the area equation in the following function
#
def area(r):
    return ______

#==============================================================================
# 3. CONCLUSION
#
# This hands-on walks you through the implementation of a script that
# computes the area of a circle.
#
# You should have learned
#
# a) how to structure a python script so it can be used as a command
#    line program.
#
# b) how to use functions
#
#==============================================================================
# 1. MAIN SECTION
#
# In software engineering, it is useful to break a program into
# multiple smaller functions so you can test each function
# independently.  In such a case, you will need a "driver script" that
# process the command line argument and pass them to the different
# functions.  We will do exactly this in this main section.

# Import the standard `argparse` package to help us process command
# line input.
import argparse

# Documentation is very important in programming.  So let's provide a
# short description of this program, which I simply copied from the
# comment at the beginning of this script.
parser = argparse.ArgumentParser(description="""
This program takes exactly one argument from the command line,
interpret it as the radius of a circle, and then compute and print out
the area of the circle.
""")

# We want this program to take exactly 1 arguments.
parser.add_argument("r", type=float, help="the radius of a circle")

# Actually parse the command line arguments.
args = parser.parse_args()

# You can test the effect of the above line by typing:
#
#     ./area.py
#
# in your command line.  It will tell you the program requires one
# argument `r`.  You may type
#
#     ./area.py -h
#
# to see the help page and find out the meanings of `r`.  Note that,
# the above line would terminate this program if you don't give it an
# argument.  So nothing below would be executed.

#------------------------------------------------------------------------------
# Now, assume you paid attention to the command line and typed in
# three arguments:
#
#    ./area.py 1
#
# Let's print out the area equation to tell the user that what
# this program is solving.
#
# Let's first assign the command line arguments back to variables
r = args.r

print("Compute the area of a circle with radius", r, " using the equation A = pi r^2.")

# However, this script cannot solve anything yet.  To start
# programming an area solver, you need to
#
# TODO: uncomment the following lines
#
# and then jump to the section "2. AREA SOLVER"
#A = area(r)
#print("A =", A)
