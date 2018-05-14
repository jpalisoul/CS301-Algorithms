#########################################################################
#                 Assignment 4 - Sorting Algorithms                     #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (February 9, 2015)                     #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file contains the following sorting functions:                 #
#       quicksort - Implements the quick sort algorithm                 #
#       partition - A supplement function to the quicksort function     #
#                                                                       #
#########################################################################

#########################################################################
#   quicksort                                                           #
#                                                                       #
#   Takes in an unsorted array and sorts it using the quick sort        #
#   algorithm.                                                          #
#########################################################################

swaps = 0
comps = 0

def quicksort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quicksort(array, low, p-1)
        quicksort(array, p+1, high)
        

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
    print("                  Array =", array)
    print("Low =", low)
    print("High = ", high)
    print("Pivot = ", pivot)
    for j in range(low, high):
        if comps < 10:
            comps += 1
            print("    Comparison #"+str(comps),"      ", str(array[j]).rjust((j+1)*4))
        elif comps >= 10:
            comps += 1
            print("    Comparison #"+str(comps),"     ", str(array[j]).rjust((j+1)*4))
        if array[j] <= pivot:
            array[i],array[j] = array[j],array[i]
            swaps += 1
            if swaps < 10:
                print("    Swap #"+str(swaps), end="")
                print("              ", end="")
                if i-j <= 2 and i-j > 1:
                    print(str(array[j]).rjust(j*4)+str(array[i]).rjust((j-i)*4))
                elif i-j >2:
                    print(str(array[j]).rjust(j*4-4)+str(array[i]).rjust((j-i)*4))
                elif i-j <= 1:
                    print(str(array[j]).rjust(j*4+4)+str(array[i]).rjust(4))
            elif swaps >= 10:
                print("    Swap #"+str(swaps), end="")
                print("            ", end="")
                if i-j <= 2 and i-j > 1:
                    print(str(array[j]).rjust(j*4)+str(array[i]).rjust((j-i)*4))
                elif i-j >2:
                    print(str(array[j]).rjust(j*4-4)+str(array[i]).rjust((j-i)*4))
                elif i-j <= 1:
                    print(str(array[j]).rjust(j*4+4)+str(array[i]).rjust(4))
            i = i + 1

    array[high],array[i]=array[i],array[high]
    return i

def reset():
    global swaps, comps
    swaps = 0
    comps = 0

def printanalysis():
    global swaps, comps
    print("\nAnalysis:")
    comps = comps-1
    print("    Comparisons:  ", comps)
    swaps = swaps-1
    print("    Swaps:        ", swaps)
    work = (comps+(swaps*5))
    print("    Work:         ", work)


##print("Swap #"+str(swaps), array[j],"  " ,array[i])
##    print("Low =", low)
##    print("High = ", high)
##    print("Pivot = ", pivot)
