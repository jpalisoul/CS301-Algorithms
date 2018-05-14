#########################################################################
#                 Assignment 3 - Sorting Algorithms (Tester)            #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (February 1, 2015)                     #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file serves as a tester for the following algorithms:          #
#       bubblesort                                                      #
#       insertionsort                                                   #
#       selectionsort                                                   #
#                                                                       #
#   EXTERNAL FILES                                                      #
#   The tested functions are in the following files:                    #
#       PalisoulJosephSort.py                                           #
#                                                                       #
#########################################################################

from PalisoulJosephSort import bubblesort, insertionsort, selectionsort

print("Joe Palisoul")
print("Assignment 3 - Sorting Algorithms\n")
print("******************************************************************\n")
print("Bubble Sort\n")

#base array
array = [3,1,4,1,5,9,2,6]

#bubble sort
bubblesort(array, 1, 1, 1)

print("\n******************************************************************")
print("Insertion Sort\n")

#base array
array = [3,1,4,1,5,9,2,6]

#insertion sort
insertionsort(array, 1, 1, 1)

print("\n******************************************************************")
print("Selection Sort\n")

#base array
array = [3,1,4,1,5,9,2,6]

#selection sort
selectionsort(array, 1, 1, 1)
