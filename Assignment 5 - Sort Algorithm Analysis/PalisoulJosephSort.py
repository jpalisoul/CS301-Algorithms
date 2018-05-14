#########################################################################
#                 Assignment 5 - Sorting Analysis                       #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (February 16, 2015)                    #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file contains the following sorting functions:                 #
#       bubblesort - Implements the bubble sort algorithm               #
#       insertionsort - Implements the insertions sort algorithm        #
#       selectionsort - Implements the selection sort algorithm         #
#       quicksort - Implements the quick sort algorithm                 #
#       quicksortoutput - loops the quicksort function                  #
#       bubblesortoutput - loops the bubblesort function                #
#       insertionsortoutput - loops the insertionsort function          #
#       selectionsortoutput - loops the selectionsort function          #
#       partition - A supplement function to the quicksort function     #
#       maxkey - A sub function used in the selectionsort algorithm     #
#                                                                       #
#########################################################################

import random

#########################################################################
#   bubblesort                                                          #
#                                                                       #
#   Takes in an unsorted array and sorts it using the bubble sort       #
#   algorithm.                                                          #
#########################################################################

def bubblesort(array, swaps, comps, loops):
    i=0
    j=1
    n = len(array)
    for i in range (n-1):
        loops = loops+1
        for j in range (n-1):
            comps = comps+1
            if array[j] > array[j+1]:
                swaps = swaps+1
                array[j+1],array[j] = array[j],array[j+1]
                j = j+1
    return(array, comps)

#########################################################################
#   bubblesortoutput                                                    #
#                                                                       #
#   Takes an Input from the tester call and repeats the bubblesort      #
#   algorithm 100 times for array sizes of "arraylength" and prints     #
#   the average number of comparisons required to sort the array.       #
#########################################################################

def bubblesortoutput(arraylength):
    sum = 0
    for count in range(100):
        array = random.sample(range(1, arraylength+1), arraylength)
        result = bubblesort(array, 1, 1, 1)
        comps = result[1]
        sum = sum + comps
    print('%11d %20.2f'%(arraylength, sum/100))
    
    
    

#########################################################################
#   insertionsort                                                       #
#                                                                       #
#   Takes in an unsorted array and sorts it using the insertion sort    #
#   algorithm.                                                          #
#########################################################################

def insertionsort(array, swaps, comps, loops):
    i=1
    n = len(array)
    for i in range (1, n):
        j=i
        loops = loops+1
        if j > 0 and array[j-1] > array[j]:
            while j > 0 and array[j-1] > array[j]:
                comps = comps+1
                swaps = swaps+1
                array[j-1],array[j] = array[j],array[j-1]
                j -= 1
        elif j > 0 and array[j-1] <= array[j]:
            comps = comps+1
            j -= 1
    return(array, comps)

#########################################################################
#   insertionsortoutput                                                 #
#                                                                       #
#   Takes an Input from the tester call and repeats the bubblesort      #
#   algorithm 100 times for array sizes of "arraylength" and prints     #
#   the average number of comparisons required to sort the array.       #
#########################################################################

def insertionsortoutput(arraylength):
    sum = 0
    for count in range(100):
        array = random.sample(range(1, arraylength+1), arraylength)
        result = insertionsort(array, 1, 1, 1)
        comps = result[1]
        sum = sum + comps
    print('%11d %20.2f'%(arraylength, sum/100))
            
                

#########################################################################
#   selection sort                                                      #
#                                                                       #
#   Takes in an unsorted array and sorts it using the selection sort    #
#   algorithm.                                                          #
#########################################################################

def selectionsort(array, swaps, comps, loops):
    n = len(array)
    maxkey.count = 0
    for i in range (n-1, 0,-1):
        loops = loops+1
        max = maxkey(0, i, array)
        swaps = swaps + 1
        array[i],array[max] = array[max],array[i]
    return(array, maxkey.count)

#########################################################################
#   selectionsortoutput                                                 #
#                                                                       #
#   Takes an Input from the tester call and repeats the bubblesort      #
#   algorithm 100 times for array sizes of "arraylength" and prints     #
#   the average number of comparisons required to sort the array.       #
#########################################################################
        
def selectionsortoutput(arraylength):
    sum = 0
    for count in range(100):
        array = random.sample(range(1, arraylength+1), arraylength)
        result = selectionsort(array, 1, 1, 1)
        comps = result[1]
        sum = sum + comps
    print('%11d %20.2f'%(arraylength, sum/100))        

#########################################################################
#   maxkey                                                              #
#                                                                       #
#   A supplement function to the selectionsort function                 #
#########################################################################

def maxkey(low, high, array):
    largest = low
    for j in range (low+1, high+1):
        maxkey.count += 1
        if array[largest] < array[j]:
            largest = j
    return largest

#########################################################################
#   quicksort                                                           #
#                                                                       #
#   Takes in an unsorted array and sorts it using the quick sort        #
#   algorithm.                                                          #
#########################################################################

swaps = 0
comps = 0

def quicksort(array, low, high):
    sum = 0
    if low < high:
        p = partition(array, low, high)
        comps = p[1]
        sum += comps
        quicksort(array, low, p[0]-1)
        quicksort(array, p[0]+1, high)
    return(array, sum)

#########################################################################
#   quicksortoutput                                                     #
#                                                                       #
#   Takes an Input from the tester call and repeats the bubblesort      #
#   algorithm 100 times for array sizes of "arraylength" and prints     #
#   the average number of comparisons required to sort the array.       #
#########################################################################

def quicksortoutput(arraylength):
    sum = 0
    for count in range(100):
        array = random.sample(range(1, arraylength+1), arraylength)
        result = quicksort(array, 0, len(array)-1)
        comps = result[1]
        sum = sum + comps
    print('%11d %20.2f'%(arraylength, sum/10000))        

#########################################################################
#   partition                                                           #
#                                                                       #
#   This is a supplement function to the quicksort function. It         #
#   serves as the mean by which the values are swapped in the function  #
#   quicksort.                                                          #
#########################################################################

def partition(array, low, high):
    global comps, swaps
    pivot = array[high]
    i = low
    for j in range(low, high):
        comps += 1
        if array[j] <= pivot:
            array[i],array[j] = array[j],array[i]
            swaps += 1
            i = i + 1
    array[high],array[i]=array[i],array[high]
    return(i, comps)
