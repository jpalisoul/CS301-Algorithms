#########################################################################
#                 Assignment 1 - Searching Algorithms                   #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (January 10, 2015)                     #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file contains the following seaching functions:                #
#       linearSearch - Implements the linear search algorithm           #
#       binarySearch - Implements the recursive binary search algorithm #
#                                                                       #
#########################################################################


#########################################################################
#   linearSearch                                                        #
#                                                                       #
#   Looks for a specific target within an unsorted list of integers.    #
#   Returns the index of the first occurrence of the target. If the     #
#   targer is not in the list, -1 is returned                           #
#########################################################################

def linearSearch(target, array):
    i=0
    print("PROBE  INDEX  VALUE   RESULT")
    for i in range(len(array)):
        if array[i] == target:
            print(str(i+1).rjust(3), str(i).rjust(6), str(array[i]).rjust(7), str("target").rjust(9))
            print("Target found in ", i+1, "probes")
            return i
        else:
            print(str(i+1).rjust(3), str(i).rjust(6), str(array[i]).rjust(7), str("not target").rjust(13))
    print("Target not found, required", i+1 ,"probes")
    return -1

#########################################################################
#   binsearch                                                           #
#                                                                       #
#   Looks for a specific target within a sorted list of integers.       #
#   Returns the index of the location of the target. If the target      #
#   is not in the list, -1 is returned.                                 #
#########################################################################

def binsearch(target, array, left, right, probe):
    if left <= right:
        mid = (left + right)//2
        if array[mid] == target:
            print(str(probe+1).rjust(3), str(left).rjust(6), str(right).rjust(6), str(mid).rjust(5), str(array[mid]).rjust(5), str("target").rjust(9))
            print("Target found in", probe+1 ,"probes")
            return mid
        elif array[mid] < target:
            print(str(probe+1).rjust(3), str(left).rjust(6), str(right).rjust(6), str(mid).rjust(5), str(array[mid]).rjust(5), str("not target, upper half").rjust(25))
            return binsearch(target, array, mid+1, right, probe+1)
        else:
            print(str(probe+1).rjust(3), str(left).rjust(6), str(right).rjust(6), str(mid).rjust(5), str(array[mid]).rjust(5), str("not target, lower half").rjust(25))
            return binsearch(target, array, left, mid-1, probe+1)
    else:
        print("Target not found, required", probe ,"probes")
        return -1


