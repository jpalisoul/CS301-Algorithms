#########################################################################
#                 Assignment 6 - Hash Tables(Jump)                      #
#                                                                       #
#   PROGRAMMED BY   Joe Palisoul (February 24, 2015)                    #
#   CLASS           CS301, Spring 2016                                  #
#   INSTRUCTOR      Dean Zeller                                         #
#                                                                       #
#   DESCRIPTION                                                         #
#   This file contains the following Hashing functions:                 #
#       arrayGetUser                                                    #   
#       printArray                                                      #               
#       hashAnalysis                                                    #
#       hashsearch                                                      #
#       hashSearchAnalysis                                              #
#                                                                       #
#########################################################################
global collisions, records, probetotal, searchtotal
collisions = 0
records = 1
probetotal = 0
searchtotal = 0
namearray=[0]*100
idarray=[0]*100

def arrayGetUser(name, idnum):
    global collisions, records
    print("Enter Record #"+str(records)+":")
    idnumshort = idnum%100
    print("    Name:   "+str(name))
    print("    ID:     "+str(idnum))
    while idarray[idnumshort] != 0:
        collisions += 1
        print("    Calculating hashing index: ", idnumshort, " (Collision #"+str(collisions)+" - " + str(namearray[idnumshort])+","+str(idarray[idnumshort])+")")
        idnumshort = (idnumshort+3)%100
    namearray[idnumshort] = name
    idarray[idnumshort] = idnum
    print("    Calculating hashing index: ", idnumshort, " (empty)")
    print("    Storing in location: ", idnumshort)
    records += 1
    print("")

def printArray():
    print("Current Table:")
    print("    INDEX    NAME     ID")
    for i in range(100):
        if idarray[i] != 0:
            print(str(i).rjust(8), str(namearray[i]).rjust(8), str(idarray[i]).rjust(9))
    print("")
            
def hashAnalysis():
    global collisions, records
    print("Table complete. ", records-1,"records in 100 spaces, with", collisions, "collisions.\n")

def hashsearch(idnum):
    global probetotal, searchtotal
    searchtotal += 1
    probe=0
    print("Search #"+str(searchtotal)+":")
    print("    Enter ID: ", idnum)
    idnumshort = idnum%100
    if idarray[idnumshort] == 0:
        print("    Calculated Index: ", idnumshort, "(empty)")
        print("    Not in table.")
        probe += 1
    elif idarray[idnumshort] == idnum:
        print("    Calculated Index: ", idnumshort, "("+ str(namearray[idnumshort])+", "+str(idarray[idnumshort])+")")
        print("    Found at index", str(idnumshort)+".")
        probe += 1
    else:
        while idarray[idnumshort] != idnum and idarray[idnumshort] != 0:
            print("    Calculated Index: ", idnumshort, "("+ str(namearray[idnumshort])+", "+str(idarray[idnumshort])+")")
            idnumshort = (idnumshort+3)%100
            probe += 1
        if idarray[idnumshort] == 0:
            print("    Calculated Index: ", idnumshort, "(empty)")
            print("    Not in table.")
            probe += 1
        else:
            print("    Calculated Index: ", idnumshort, "("+ str(namearray[idnumshort])+", "+str(idarray[idnumshort])+")")
            print("    Found at index", str(idnumshort)+".")
            probe += 1
    if probe < 2:
        print("    Required", probe, "probe.\n")
    else:
        print("    Required", probe, "probes.\n")
    probetotal += probe

def hashSearchAnalysis():
    global probetotal, seachtotal
    average = probetotal/searchtotal
    print("Summary:  Performed", searchtotal, "searches, requiring", probetotal, "probes,")
    print("          for an average of", average, "probes per search")
