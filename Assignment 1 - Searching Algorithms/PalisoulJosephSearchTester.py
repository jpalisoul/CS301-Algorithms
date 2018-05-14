#########################################################################
#                 Assignment 1 - Searching Algorithms (Tester)          #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (January 10, 2015)                     #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file serves as a tester for the following algorithms:          #
#       linearSearch                                                    #
#       binarySearch                                                    #
#                                                                       #
#   EXTERNAL FILES                                                      #
#   The tested functions are in the following files:                    #
#       PalisoulJosephSearch.py                                         #
#                                                                       #
#########################################################################

from PalisoulJosephSearch import linearSearch
from PalisoulJosephSearch import binsearch

print("Joe Palisoul")
print("Assignment 1 - Searching Algorithms\n")
print("******************************************************************\n")
print("Part 1 - Linear Search\n")
array = [31,41,59,24,53,58,97,93,23,84,62,64,33,83,27,95]
print ("array = [31,41,59,24,53,58,97,93,23,84,62,64,33,83,27,95]\n")
target = 62
print("target: 62")
linearSearch(target, array)

target = 59

print("\ntarget: 59")
linearSearch(target, array)

target = 37

print("\ntarget: 37")
linearSearch(target, array)

array = [23,24,27,31,33,41,53,58,59,62,64,83,84,93,95,97]
target = 62
length = len(array)-1

print("\n******************************************************************\n")
print("Part 2 - Binary Search\n")
print("array = [23,24,27,31,33,41,53,58,59,62,64,83,84,93,95,97]\n")
print("target: 62")
print("PROBE  LEFT  RIGHT  MID  VALUE   RESULT")
binsearch(target, array, 0, length, 0)

target = 59

print("\ntarget: 59")
print("PROBE  LEFT  RIGHT  MID  VALUE   RESULT")
binsearch(target, array, 0, length, 0)

target = 37

print("\ntarget: 37")
print("PROBE  LEFT  RIGHT  MID  VALUE   RESULT")
binsearch(target, array, 0, length, 0)



















