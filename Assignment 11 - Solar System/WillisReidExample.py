###########################################################################
#                 Assignment 4 -- Primitive Animation, Part 2             #
#                            Solar System                                 #
#                                                                         #
#  Programmed by Reid Willis (11/2/2015)                                  #
#  Instructor:  Dean Zeller                                               #
#                                                                         #
#  Description:  This program uses Tkinter methods to animate a circle    #
#                moving around on the canvas.                             #
#                                                                         #
#  This program is copyright (c) 2015 Reid Willis and Dean Zeller.        #
#  All rights reserved.  Permission granted to use and modify for         #
#  educational purposes only.  Any commercial use of this code must       #
#  receive permission from the author(s).                                 #
###########################################################################
from tkinter import *
import math
import random
c = Canvas(width=650,height=650,bg="black")
c.pack(expand=YES, fill=BOTH)

# Set delay speed variable for overall animation speed
shortDelay=50
mediumDelay=500
longDelay=1000

# Find the centerpoint of an object
def center(objectID):
    x1 = c.coords(objectID)[0]
    y1 = c.coords(objectID)[1]
    x2 = c.coords(objectID)[2]
    y2 = c.coords(objectID)[3]
    
    x = x1 + ( (x2-x1) / 2)
    y = y1 + ( (y2-y1) / 2)

    return([x,y])

# Move an object to the next point along its rotation
def orbit_step(orbiter, orbited, radius="100", rotations=1):
    angle = i * rotations
    c.move(orbiter, -1 * c.coords(orbiter)[0], -1 * c.coords(orbiter)[1])
    x_cord = radius * math.cos(math.radians(angle)) + center(orbited)[0]
    y_cord = radius * math.sin(math.radians(angle)) + center(orbited)[1]
    c.move(orbiter, x_cord, y_cord)
    c.after(5)

# Calculate a random position along an orbit of given radius 
def circle_point(orbited, radius):
    angle = random.randrange(0,360,1)
    x_cord = radius * math.cos(math.radians(angle)) + center(orbited)[0]
    y_cord = radius * math.sin(math.radians(angle)) + center(orbited)[1]
    return([x_cord,y_cord])

# Draw solar system
c.create_oval(275,275, 375,375, fill="yellow", tag="sun")
c.create_oval(0,0, 20,20, fill="green", tag="earth")
c.create_oval(0,0, 8,8, fill="white", tag="moon")
c.create_oval(0,0, 17,17, fill="olive", tag="venus")
c.create_oval(0,0, 10,10, fill="#755C51", tag="mercury")
c.create_oval(0,0, 13,13, fill="red", tag="mars")

# Generate asteroid belt
for i in range(500):
    current_asteroid = "asteroid_" + str(i)
    asteroid_x = random.randrange(5,7)
    asteroid_y = random.randrange(5,7)
    position = circle_point("sun", random.randrange(250,300))
    c.create_oval(0,0,asteroid_x,asteroid_y, fill="white", tag=current_asteroid)
    c.move(current_asteroid, position[0], position[1])

# Simulate Orbits of planets/moons
for i in range(4680):
    orbit_step("mars", "sun", 210, 0.53)
    orbit_step("earth", "sun", 150, 1)
    orbit_step("moon", "earth", 25, 12)
    orbit_step("venus", "sun", 100, 1.62)
    orbit_step("mercury", "sun", 75, 4.15)

    # Optional little treat. Uncomment to see the cool pattern the orbits draw!
    #if i%3 == 0:
    #    mars_pos = center("venus")
    #    mercury_pos = center("earth")
    #    c.create_line(mars_pos[0],mars_pos[1], mercury_pos[0],mercury_pos[1],
    #                  fill="white")
    
    c.update()
