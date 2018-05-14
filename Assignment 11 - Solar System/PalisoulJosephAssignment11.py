###########################################################################
#                    Assignment 11 -- Orbit Paths                         #
#                            Solar System                                 #
#                                                                         #
#  Programmed by Joseph Palisoul (4/8/2016)                               #
#  Instructor:  Dean Zeller                                               #
#                                                                         #
#  Description:  This program uses Tkinter methods to animate a circle    #
#                moving around on the canvas.                             #
#                                                                         #
#  This program is copyright (c) 2016 Joseph Palisoul and Dean Zeller.    #
#  All rights reserved.  Permission granted to use and modify for         #
#  educational purposes only.  Any commercial use of this code must       #
#  receive permission from the author(s).                                 #
###########################################################################
from tkinter import *
import math
import random

###########################################################################
# delay(time) -- Pause the animation for the given time, in milliseconds. #
###########################################################################
def delay(time):
    c.after(time)
    c.update()

# Set delay speed variable for overall animation speed
shortDelay=50
mediumDelay=500
longDelay=1000


# Initial variables

# Galaxy
size = 1000
galX = size/2
galY = size/2
numStars = 500
starColor = "white"
c = Canvas(width=size,height=size,bg="black")
c.pack(expand=YES, fill=BOTH)
photo = PhotoImage(file = './gif.gif')
enterpriseX = 500
enterpriseY = -800



# Sun
sunR = 40
sunColor = "yellow"

# Mercury
mercuryOrbitR = 58
mercuryR = 3
mercuryColor = "orange"
mercuryOrbitDelta = -10.36
mercuryStartTheta = 90

# Enterprise
enterpriseOrbitR = 15
enterpriseR = 8
enterpriseColor = "grey"
enterpriseOrbitDelta = -2
enterpriseStartTheta = 90

# Venus
venusOrbitR = 73
venusR = 5
venusColor = "orange2"
venusOrbitDelta = -3.24
venusStartTheta = -45

# Earth
earthR = 10
earthColor = "blue"
earthOrbitR = 130
earthOrbitDelta = -2

# Moon
moonOrbitR = 25
moonR = 4
moonColor = "grey75"
moonOrbitDelta = -26

# Mars
marsOrbitR = 175
marsR = 8
marsColor = "red2"
marsOrbitDelta = -1.06

# Jupiter
jupiterR = 40
jupiterColor = "salmon"
jupiterOrbitR = 280
jupiterOrbitDelta = -.168

# Titan
titanOrbitR = 60
titanR = 8
titanColor = "aqua"
titanOrbitDelta = -2

# Saturn
saturnR = 32
saturnColor = "red4"
saturnOrbitR = 370
saturnOrbitDelta = -.0678
saturnStartTheta = 135

# Uranus
uranusR = 20
uranusColor = "lightblue"
uranusOrbitR = 430
uranusOrbitDelta = -.023778
uranusStartTheta = 228

# Neptune
neptuneR = 16
neptuneColor = "blue3"
neptuneOrbitR = 470
neptuneOrbitDelta = -.01212

# Draw stars
for i in range(numStars):
    x = random.randrange(size)
    y = random.randrange(size)
    starR = 1
    c.create_oval(x-starR,y-starR,x+starR,y+starR,
                  fill=starColor)

previousX = 0
previousY = 0
titanX = 0
titanY = 0
for i in range(1000):
    c.delete("enterprise")
    c.delete("planet")
    c.create_oval(galX-sunR,galY-sunR,galX+sunR,galY+sunR,
                  fill=sunColor, tag="planet")   # sun

    theta = (mercuryStartTheta + mercuryOrbitDelta*i)*3.14/180
    mercuryX = galX+mercuryOrbitR*math.cos(theta)
    mercuryY = galY+mercuryOrbitR*math.sin(theta)
    c.create_oval(mercuryX-mercuryR,
                  mercuryY-mercuryR,
                  mercuryX+mercuryR,
                  mercuryY+mercuryR,
                  fill=mercuryColor, tag="planet")  # mercury

    theta = (venusStartTheta + venusOrbitDelta*i)*3.14/180
    venusX = galX+venusOrbitR*math.cos(theta)
    venusY = galY+venusOrbitR*math.sin(theta)
    c.create_oval(venusX-venusR,
                  venusY-venusR,
                  venusX+venusR,
                  venusY+venusR,
                  fill=venusColor, tag="planet")  # venus
    
    theta = earthOrbitDelta*i*3.14/180
    earthX = galX+earthOrbitR*math.cos(theta)
    earthY = galY+earthOrbitR*math.sin(theta)
    c.create_oval(earthX-earthR,
                  earthY-earthR,
                  earthX+earthR,
                  earthY+earthR,
                  fill=earthColor, tag="planet")  # earth
    
    theta = moonOrbitDelta*i*3.14/180
    moonX = earthX+moonOrbitR*math.cos(theta)
    moonY = earthY+moonOrbitR*math.sin(theta)
    c.create_oval(moonX-moonR,
                  moonY-moonR,
                  moonX+moonR,
                  moonY+moonR,
                  fill=moonColor, tag="planet")  # moon

    theta = marsOrbitDelta*i*3.14/180
    marsX = galX+marsOrbitR*math.cos(theta)
    marsY = galY+marsOrbitR*math.sin(theta)
    c.create_oval(marsX-marsR,
                  marsY-marsR,
                  marsX+marsR,
                  marsY+marsR,
                  fill=marsColor, tag="planet")  # mars
    
    theta = jupiterOrbitDelta*i*3.14/180
    jupiterX = galX+jupiterOrbitR*math.cos(theta)
    jupiterY = galY+jupiterOrbitR*math.sin(theta)
    c.create_oval(jupiterX-jupiterR,
                  jupiterY-jupiterR,
                  jupiterX+jupiterR,
                  jupiterY+jupiterR,
                  fill=jupiterColor, tag="planet")  # jupiter

    theta = titanOrbitDelta*i*3.14/180
    titanX = jupiterX+titanOrbitR*math.cos(theta)
    titanY = jupiterY+titanOrbitR*math.sin(theta)
    c.create_oval(titanX-titanR,
                  titanY-titanR,
                  titanX+titanR,
                  titanY+titanR,
                  fill=titanColor, tag="planet")  # titan

    theta = (saturnStartTheta + saturnOrbitDelta*i)*3.14/180
    saturnX = galX+saturnOrbitR*math.cos(theta)
    saturnY = galY+saturnOrbitR*math.sin(theta)
    c.create_oval(saturnX-saturnR,
                  saturnY-saturnR,
                  saturnX+saturnR,
                  saturnY+saturnR,
                  fill=saturnColor, tag="planet")  # saturn

    theta = (uranusStartTheta + uranusOrbitDelta*i)*3.14/180
    uranusX = galX+uranusOrbitR*math.cos(theta)
    uranusY = galY+uranusOrbitR*math.sin(theta)
    c.create_oval(uranusX-uranusR,
                  uranusY-uranusR,
                  uranusX+uranusR,
                  uranusY+uranusR,
                  fill=uranusColor, tag="planet")  # uranus

    theta = neptuneOrbitDelta*i*3.14/180
    neptuneX = galX+neptuneOrbitR*math.cos(theta)
    neptuneY = galY+neptuneOrbitR*math.sin(theta)
    c.create_oval(neptuneX-neptuneR,
                  neptuneY-neptuneR,
                  neptuneX+neptuneR,
                  neptuneY+neptuneR,
                  fill=neptuneColor, tag="planet")  # neptune

    enterpriseY += 3
    c.create_image(enterpriseX, enterpriseY, image = photo, tag ="enterprise")
    #enterprise
    
    delay(shortDelay)
