#########################################################################
#                 Assignment 6 - Hash Tables (Tester)(Linear)           #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (February 24, 2015)                    #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file serves as a tester for the following algorithms:          #
#       Linear Hash                                                     #
#                                                                       #
#   EXTERNAL FILES                                                      #
#   The tested functions are in the following files:                    #
#       PalisoulJosephHashTable.py                                      #
#                                                                       #
#########################################################################

from PalisoulJosephHashTableLinear import arrayGetUser, printArray, hashAnalysis, hashsearch, hashSearchAnalysis

print("Joseph Palisoul")
print("Assignment 6 - Hash Tables\n")
print("***************************************************************************")
print("Hash Algorithm #1 - Standard Linear")
print("***************************************************************************\n")
print("************************* --> Building the Table <-- **********************\n")

#creating and printing array
arrayGetUser("Dean", 31415)
printArray()
arrayGetUser("Megan", 21423)
printArray()
arrayGetUser("Gracie", 66467)
printArray()
arrayGetUser("Jonny", 24608)
printArray()
arrayGetUser("Cody", 10727)
printArray()
arrayGetUser("Davon", 12995)
printArray()
arrayGetUser("Kayla", 94537)
printArray()
arrayGetUser("Coley", 10851)
printArray()
arrayGetUser("Ellie", 44871)
printArray()
arrayGetUser("Jessie", 22015)
printArray()
arrayGetUser("Noah", 65417)
printArray()
arrayGetUser("Messy", 61516)
printArray()
hashAnalysis()

print("********************** --> Searching the Table <-- **********************")

#searching the hash table
hashsearch(60241)
hashsearch(31415)
hashsearch(68215)
hashsearch(61516)
hashSearchAnalysis()
