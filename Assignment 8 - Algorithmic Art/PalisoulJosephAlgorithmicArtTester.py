###########################################################################
#                        Algorithmic Art Tester                           #
#                                                                         #
#  Programmed by Joseph Palisoul (03-28-2016)                             #
#                                                                         #
#  The following is a tester for the Algorithmic Art assignment.          #
#                                                                         #
#  EXTERNAL FILES                                                         #
#  The following external files are used in the process of running the    #
#  animation.                                                             #
#       PalisoulJosephAlgorithmicArt, written by Joseph Palisoul          #
#               ConnectTheDots    Connect every dot to every other dot    #
#               triagles          Generates random triangles              #
#               circles           Generates random circles                #
###########################################################################
from PalisoulJosephAlgorithmicArt import circles, triangles, ConnectTheDots
import random
from tkinter import *
canvasWidth = 1000
canvasHeight = 500
c = Canvas(width=canvasWidth, height=canvasHeight, bg='white')
c.pack(expand=YES, fill=BOTH)


circles(c, canvasWidth=canvasWidth, canvasHeight=canvasHeight, radius=50, numCircles=50,
        fillList=["yellow", "red", "green", "blue", "purple"])

triangles(c, numTriangles=50, startX=1100, endX=1500, startY=600, endY=1000)

ConnectTheDots(c, canvasWidth=400, canvasHeight=400, radius=5,
            numCircles=22, startX=0, endX=500, startY=600, endY=1000,
            lineWidth=1, lineColor="black", fillList=["black"])

