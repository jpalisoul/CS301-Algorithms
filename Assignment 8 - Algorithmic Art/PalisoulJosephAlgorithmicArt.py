###########################################################################
#                  Assignment 8 -- Algorithmic Art                        #
#                                                                         #
#  Programmed by Joseph Palisoul 3-28-2016                                #
#  Instructor:  Dean Zeller                                               #
#                                                                         #
#  Description:  The file contains functions to draw three different      #
#                forms of algorithmic art.                                #
#                                                                         #
#  Functions:                                                             #
#               ConnectTheDots    Connect every dot to every other dot    #
#               triagles          Generates random triangles              #
#               circles           Generates random circles                #      #
#                                                                         #
#  This program is copyright (c) 2016 Joseph Palisoul and Dean Zeller.    #
#  All rights reserved.  Permission granted to use and modify for         #
#  educational purposes only.  Any commercial use of this code must       #
#  receive permission from the authors.                                   #
###########################################################################
from tkinter import *
import random

###########################################################################
#               circles           Generates random circles                # 
###########################################################################

def circles(c, canvasWidth=400, canvasHeight=400, radius=100, numCircles=10,
            lineWidth=1, lineColor="black", fillList=["black"]):
    points = []
    for i in range(numCircles):
        centerX=random.randrange(canvasWidth)
        centerY=random.randrange(canvasHeight)
        points.append((centerX, centerY))
    for p in points:
        color=random.choice(fillList)
        c.create_oval(p[0]-radius, p[1]-radius,
                      p[0]+radius, p[1]+radius,
                      fill=color)
        c.after(50)
        c.update()

###########################################################################
#               triagles          Generates random triangles              #
###########################################################################

def triangles(c, numTriangles=50, startX=500, endX=1000, startY=300, endY=500,
              lineWidth=1, lineColor="black", color=["black"]):
    color = ["red", "orange", "yellow", "blue", "green", "pink", "purple"]
    for i in range(numTriangles):
             x1 = random.randint(startX, endX)
             x2 = random.randint(startX, endX)
             x3 = random.randint(startX, endX)
             y1 = random.randint(startY, endY)
             y2 = random.randint(startY, endY)
             y3 = random.randint(startY, endY)
             c.create_polygon(x1, y1, x2, y2, x3, y3, fill=random.choice(color))
             c.after(50)
             c.update()

###########################################################################
#               ConnectTheDots    Connect every dot to every other dot    #
###########################################################################

def ConnectTheDots(c, canvasWidth=400, canvasHeight=400, radius=5,
            numCircles=50, startX=0, endX=500, startY=500, endY=1000,
            lineWidth=1, lineColor="black", fillList=["black"]):
    points = []
    fillList=["yellow", "red", "green", "blue", "purple"]
    for i in range(numCircles):
        centerX=random.randint(startX, endX)
        centerY=random.randint(startY, endY)
        points.append((centerX, centerY))
    for points1 in points:
        for points2 in points:
            c.create_line(points1, points2, width=lineWidth, fill=lineColor)
        for p in points:
            color=random.choice(fillList)
            c.create_oval(p[0]-radius, p[1]-radius,
                      p[0]+radius, p[1]+radius,
                      fill=color)









    
