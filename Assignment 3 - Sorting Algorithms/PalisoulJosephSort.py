#########################################################################
#                 Assignment 3 - Sorting Algorithms                     #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (February 1, 2015)                     #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file contains the following sorting functions:                 #
#       bubblesort - Implements the bubble sort algorithm               #
#       insertionsort - Implements the insertions sort algorithm        #
#       selectionsort - Implements the selection sort algorithm         #
#       maxkey - A sub function used in the selectionsort algorithm     #
#                                                                       #
#########################################################################

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
        print ("Loop #"+str(loops),":     Array = ", array)
        loops = loops+1
        for j in range (n-1):
            print("    Comparison #"+str(comps),end="")
            if comps < 10:
                print("       ", end="")
            elif comps >= 10:
                print("      ", end="")
            for i in range(j):
                print("   ", end="")
            print(array[j]," "+str(array[j+1]))
            comps = comps+1
            if array[j] > array[j+1]:
                print("    Swap #", swaps, end="")
                print("            ", end="")
                for i in range(j):
                    print("   ", end="")
                print(array[j+1]," "+str(array[j]))
                swaps = swaps+1
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                j = j+1
                
    print("\nAnalysis:")
    comps = comps-1
    print("    Comparisons:  ", comps)
    swaps = swaps-1
    print("    Swaps:        ", swaps)
    work = (comps+(swaps*5))
    print("    Work:         ", work)
    
    

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
        print ("Loop #",loops,":     Array = ", array)
        loops = loops+1
        if j > 0 and array[j-1] > array[j]:
            while j > 0 and array[j-1] > array[j]:
                print("    Comparison #"+str(comps),end="")
                if comps < 10:
                    print("     ", end="")
                elif comps >= 10:
                    print("    ", end="")
                for i in range(j):
                    print("   ", end="")
                print(array[j-1]," "+str(array[j]))
                comps = comps+1
                print("    Swap #", swaps, end="")
                print("          ", end="")
                for i in range(j):
                    print("   ", end="")
                print(array[j]," "+str(array[j-1]))
                swaps = swaps+1
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                j -= 1
        elif j > 0 and array[j-1] <= array[j]:
            print("    Comparison #"+str(comps),end="")
            if comps < 10:
                print("     ", end="")
            elif comps >= 10:
                print("    ", end="")
            for i in range(j):
                print("   ", end="")
            print(array[j-1]," "+str(array[j]))
            comps = comps+1
            j -= 1
            
    print("\nAnalysis:")
    comps = comps-1
    print("    Comparisons:  ", comps)
    swaps = swaps-1
    print("    Swaps:        ", swaps)
    work = (comps+(swaps*5))
    print("    Work:         ", work)
            
                

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
        print ("Loop #"+str(loops),":     Array = ", array)
        loops = loops+1
        max = maxkey(0, i, array)
        print("    Swap #"+str(swaps), end="")
        print("        ", end="")
        if i-max <= 2 and i-max > 1:
            print(str(array[i]).rjust(i*3)+str(array[max]).rjust((i-max)*3))
            swaps = swaps + 1
        elif i-max >2:
            print(str(array[i]).rjust(i*3-3)+str(array[max]).rjust((i-max)*3))
            swaps = swaps + 1
        elif i-max <= 1:
            print(str(array[i]).rjust(i*3+3)+str(array[max]).rjust(3))
            swaps = swaps + 1
        temp = array[max]
        array[max] = array[i]
        array[i] = temp

    print("\nAnalysis:")
    comps = comps-1
    print("    Comparisons:  ", maxkey.count)
    swaps = swaps-1
    print("    Swaps:        ", swaps)
    work = (maxkey.count+(swaps*5))
    print("    Work:         ", work)
        
        

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
        if maxkey.count < 10:
            print("    Comparison #"+str(maxkey.count),"      ", str(array[j]).rjust(j*3),
                  str("max=").rjust(28-j*3)+str(array[largest]), "  array["+ str(largest)+"]")
        elif maxkey.count >= 10:
             print("    Comparison #"+str(maxkey.count),"     ", str(array[j]).rjust(j*3),
                   str("max=").rjust(28-j*3)+str(array[largest]), "  array["+ str(largest)+"]")
    return largest

