#########################################################################
#                 Assignment 4 - Sorting Algorithms (Tester)            #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (February 9, 2015)                     #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file serves as a tester for the following algorithms:          #
#       quicksort                                                       #
#                                                                       #
#   EXTERNAL FILES                                                      #
#   The tested functions are in the following files:                    #
#       PalisoulJosephSort.py                                           #
#                                                                       #
#########################################################################

from PalisoulJosephSort import quicksort, printanalysis

print("Joe Palisoul")
print("Assignment 4 - Sorting Algorithms\n")
print("******************************************************************\n")
print("Quick Sort\n")

#base array
array = [69,81,22,48,13,38,93,14,45,58,79,72]

#quick sort
quicksort(array, 0, len(array)-1)
printanalysis()
print(array)


