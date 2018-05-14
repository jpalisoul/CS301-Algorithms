#########################################################################
#                 Assignment 2 - Searching Algorithms                   #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (January 22, 2015)                     #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file contains the following seaching functions:                #
#       linearSearch - Implements the linear search algorithm           #
#       binarySearch - Implements the recursive binary search algorithm #
#       linearOutput - Implements the loop of the linearSearch Function #                                                                
#       binsearchOutput - Implements the loop of the binsearch Function #                                                                    
#                                                                       #
#########################################################################

import random

#########################################################################
#   linearSearch                                                        #
#                                                                       #
#   Looks for a specific target within an unsorted list of integers.    #
#   Returns the index of the first occurrence of the target. If the     #
#   targer is not in the list, -1 is returned                           #
#########################################################################

def linearSearch(target, array):
    for i in range(len(array)):
        if array[i] == target:
            return (i,i+1)
    return (-1,i+1)

#########################################################################
#   binsearch                                                           #
#                                                                       #
#   Looks for a specific target within a sorted list of integers.       #
#   Returns the index of the location of the target. If the target      #
#   is not in the list, -1 is returned.                                 #
#########################################################################

def binsearch(target, array, left, right, probe):
    if left <= right:
        probe += 1
        mid = (left + right)//2
        if array[mid] == target:
            return (mid, probe)
        elif array[mid] < target:
            return binsearch(target, array, mid+1, right, probe)
        else:
            return binsearch(target, array, left, mid-1, probe)
    else:
        return (-1, probe)

#########################################################################
#   linearOutput                                                        #
#                                                                       #
#   Takes one input called arraylength in and repeats the linearSearch  #
#   Function (arraylength) times. Calculates the average number         #
#   of probes required and prints out the value. (Ex 5.92)              #
#########################################################################

def linearOutput(arraylength):
    sum = 0
    for count in range(arraylength):
        array = random.sample(range(1, arraylength+1), arraylength)
        target = random.choice(array)
        result = linearSearch(target, array)
        probes = result[1]
        sum = sum + probes
    print('%11d %19.2f'%(arraylength, sum/arraylength))

#########################################################################
#   binsearchOutput                                                     #
#                                                                       #
#   Takes one input called arraylength in and repeats the linearSearch  #
#   Function (arraylength) times. Calculates the average number         #
#   of probes required and prints out the value. (Ex 5.92)              #
#########################################################################

def binsearchOutput(arraylength):
    sum  = 0
    for count in range(arraylength):
        array = random.sample(range(1, arraylength+1), arraylength)
        target = random.choice(array)
        array.sort()
        result = binsearch(target, array, 0, arraylength-1, 0)
        probes = result[1]
        sum = sum + probes
    print('%11d %19.2f'%(arraylength, sum/arraylength))


