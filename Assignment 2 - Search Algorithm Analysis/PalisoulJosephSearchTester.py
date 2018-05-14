#########################################################################
#                 Assignment 2 - Searching Algorithms (Tester)          #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (January 22, 2015)                     #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file serves as a tester for the following algorithms:          #
#       linearSearch                                                    #
#       binarySearch                                                    #
#       linearOutput                                                    #
#       binsearchOutput                                                 #
#                                                                       #
#   EXTERNAL FILES                                                      #
#   The tested functions are in the following files:                    #
#       PalisoulJosephSearch.py                                         #
#                                                                       #
#########################################################################

from PalisoulJosephSearch import linearSearch, binsearch, linearOutput, binsearchOutput
import random

print("Joe Palisoul")
print("Assignment 1 - Searching Algorithms\n")
print("******************************************************************\n")
print("Part 1 - Linear Search\n")
print("     ARRAY SIZE    AVERAGE PROBES REQUIRED")

#calling output for linear search
linearOutput(10)
linearOutput(50)
linearOutput(100)
linearOutput(500)
linearOutput(1000)

print("******************************************************************\n")
print("Part 2 - Binary Search\n")
print("     ARRAY SIZE    AVERAGE PROBES REQUIRED")

#calling output for binary search
binsearchOutput(10)
binsearchOutput(50)
binsearchOutput(100)
binsearchOutput(500)
binsearchOutput(1000)




















