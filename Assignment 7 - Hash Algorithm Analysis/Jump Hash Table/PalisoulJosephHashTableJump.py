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
import random
global collisions, records, probetotal, notprobetotal, searchtotal, tries
collisions = 0
records = 0
probetotal = 0
notprobetotal = 0
searchtotal = 0
tries = 0
namearray=[0]*100
idarray=[0]*100
colarray=[0]*100
truearray=[0]*100
falsearray=[0]*100
valuearray=[0]*100

def arrayGetUser(idnum):
    global collisions, records
    collisions = 0
    idnumshort = idnum%100
    while idarray[idnumshort] != 0:
        collisions += 1
        idnumshort = (idnumshort+3)%100
    idarray[idnumshort] = idnum
    records += 1
    return(collisions)

def roundArrays():
    i=0
    for i in range(100):
        colresult = colarray[i]
        colresult = round(colresult/10, 1)
        colarray[i] = colresult
        trueresult = truearray[i]
        trueresult = round(trueresult/10, 1)
        truearray[i] = trueresult
        falseresult = falsearray[i]
        falseresult = round(falseresult/10, 1)
        falsearray[i] = falseresult
        
def printArrays():
    i=0
    print("#RECORDS    COLLISIONS    FOUND PROBES    NOT-FOUND PROBES")
    for i in range(100):
        print(str(i+1).rjust(5),str(colarray[i]).rjust(12),str(truearray[i]).rjust(15),str(falsearray[i]).rjust(15))

def hashsearch(idnum):
    global probetotal, searchtotal
    searchtotal += 1
    probe=0
    idnumshort = idnum%100
    if idarray[idnumshort] == 0:
        probe += 1
    elif idarray[idnumshort] == idnum:
        probe += 1
    else:
        while idarray[idnumshort] != idnum and idarray[idnumshort] != 0:
            idnumshort = (idnumshort+3)%100
            probe += 1
        if idarray[idnumshort] == 0:
            probe += 1
        else:
            probe += 1
    probetotal = probe
    return(-1, probetotal)

def nothashsearch(idnum):
    global notprobetotal, searchtotal
    searchtotal += 1
    notprobe=0
    idnumshort = idnum%100
    if idarray[idnumshort] == 0:
        notprobe += 1
    elif idarray[idnumshort] == idnum:
        notprobe += 1
    else:
        while idarray[idnumshort] != idnum and idarray[idnumshort] != 0:
            idnumshort = (idnumshort+3)%100
            notprobe += 1
        if idarray[idnumshort] == 0:
            notprobe += 1
        else:
            notprobe += 1
    notprobetotal = notprobe
    return(-1, notprobetotal)

##def hashSearchAnalysis():
##    global probetotal, seachtotal
##    average = probetotal/searchtotal
##    print("Summary:  Performed", searchtotal, "searches, requiring", probetotal, "probes,")
##    print("          for an average of", average, "probes per search")

def nottarget(valuearray):
    result = random.randint(10000, 99999)
    for i in range(len(valuearray)-1):
        if valuearray[i] == nottarget:
            return nottarget(valuearray)
    return(valuearray, result)

def target(valuearray):
    i=0
    result = random.choice(valuearray)
    while result == 0:
        return target(valuearray)
        i+=1
    return(valuearray, result)

def HashTestRun():
    global collisions
    
def HashTestRun():
    global collisions, records,tries
    i=0
    j=0
    s=0
    trueprobes = 0
    falseprobes = 0
    for i in range(len(valuearray)):
        valuearray[i] = 0
        idarray[i] = 0
    tries+=1
    for j in range(99):
        value = random.randint(10000, 99999)
        valuearray[j] = value
        arrayGetUser(value)#adding a member to the hash table
        colarray[j] += collisions
        collisions = 0
        trueprobes = 0
        falseprobes = 0
        for s in range(10):
            result1 = target(valuearray)
            input1 = result1[1]
            search = hashsearch(input1)
            trueprobes = search[1]
            result2 = nottarget(valuearray)
            input2 = result2[1]
            notsearch = nothashsearch(input2)
            falseprobes = notsearch[1]
            truearray[j] += trueprobes/10
            falsearray[j] += falseprobes/10
