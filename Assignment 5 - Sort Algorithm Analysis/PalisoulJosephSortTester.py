#########################################################################
#                 Assignment 4 - Sorting Analysis (Tester)              #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (February 16, 2015)                    #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file serves as a tester for the following algorithms:          #
#       quicksortoutput                                                 #
#       bubblesortoutput                                                #
#       insertionsortoutput                                             #
#       selectionsortoutput                                             #
#                                                                       #
#   EXTERNAL FILES                                                      #
#   The tested functions are in the following files:                    #
#       PalisoulJosephSort.py                                           #
#                                                                       #
#########################################################################

from PalisoulJosephSort import bubblesortoutput, insertionsortoutput, quicksortoutput, selectionsortoutput
print("Joe Palisoul")
print("Assignment 5 - Sorting Algorithms Analysis\n")
print("******************************************************************\n")
print("Sort 1 - Bubble Sort\n")
print("     ARRAY SIZE    AVERAGE COMPS REQUIRED")
#bubblesort
bubblesortoutput(10)
bubblesortoutput(50)
bubblesortoutput(100)
bubblesortoutput(500)
bubblesortoutput(1000)
print("\n******************************************************************\n")
print("Sort 2 - Insertion Sort\n")
print("     ARRAY SIZE    AVERAGE COMPS REQUIRED")
#insertionsort
insertionsortoutput(10)
insertionsortoutput(50)
insertionsortoutput(100)
insertionsortoutput(500)
insertionsortoutput(1000)
print("\n******************************************************************\n")
print("Sort 3 - Selection Sort\n")
print("     ARRAY SIZE    AVERAGE COMPS REQUIRED")
#selectionsort
selectionsortoutput(10)
selectionsortoutput(50)
selectionsortoutput(100)
selectionsortoutput(500)
selectionsortoutput(1000)
print("\n******************************************************************\n")
print("Sort 4 - Quick Sort\n")
print("     ARRAY SIZE    AVERAGE COMPS REQUIRED")
#quicksort
quicksortoutput(10)
quicksortoutput(50)
quicksortoutput(100)
quicksortoutput(500)
quicksortoutput(1000)

