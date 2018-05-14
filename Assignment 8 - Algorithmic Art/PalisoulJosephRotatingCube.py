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
#       PalisoulJosephAlgorithmicArt, written by Joseph Palisoul and      #
#                                     Justin Raines                       #
###########################################################################

from tkinter import *
from math import *
import time

class App:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.width,height=self.height)
        self.root.bind("<Key>", key)
        
    def final(self):
        self.canvas.pack()
        self.root.after(0, go())
        self.root.mainloop()
    
class Cube:
    def __init__(self,canvas,origin,size):
        self.origin = origin
        self.size = size
        self.canvas = canvas
        self.inital()
        self.draw()

    def inital(self):
        self.half = [self.origin[0]- (self.size/2),
                     self.origin[1]- (self.size/2),
                     self.origin[2]- (self.size/2)]
        self.p1 = [self.half[0],self.half[1],self.half[2]]
        self.p2 = [self.half[0] + self.size,self.half[1],self.half[2]]
        self.p3 = [self.half[0] + self.size,self.half[1],self.half[2] + self.size]
        self.p4 = [self.half[0],self.half[1],self.half[2] + self.size]
        self.p5 = [self.half[0],self.half[1] + self.size,self.half[2]]
        self.p6 = [self.half[0] + self.size,self.half[1] + self.size,self.half[2]]
        self.p7 = [self.half[0] + self.size,self.half[1] + self.size,self.half[2] + self.size]
        self.p8 = [self.half[0],self.half[1] + self.size,self.half[2] + self.size]
        
    def draw(self):
        p1x,p1y = self.p1[0],self.p1[1]
        p2x,p2y = self.p2[0],self.p2[1]
        p3x,p3y = self.p3[0],self.p3[1]
        p4x,p4y = self.p4[0],self.p4[1]
        p5x,p5y = self.p5[0],self.p5[1]
        p6x,p6y = self.p6[0],self.p6[1]
        p7x,p7y = self.p7[0],self.p7[1]
        p8x,p8y = self.p8[0],self.p8[1]
        
        self.l12 = self.canvas.create_line(p1x,p1y,p2x,p2y,fill="Blue")
        self.l23 = self.canvas.create_line(p2x,p2y,p3x,p3y,fill="Blue")
        self.l34 = self.canvas.create_line(p3x,p3y,p4x,p4y,fill="Blue")
        self.l14 = self.canvas.create_line(p1x,p1y,p4x,p4y,fill="Blue")
        self.l15 = self.canvas.create_line(p1x,p1y,p5x,p5y,fill="green")
        self.l26 = self.canvas.create_line(p2x,p2y,p6x,p6y,fill="green")
        self.l37 = self.canvas.create_line(p3x,p3y,p7x,p7y,fill="green")
        self.l48 = self.canvas.create_line(p4x,p4y,p8x,p8y,fill="green")
        self.l56 = self.canvas.create_line(p5x,p5y,p6x,p6y,fill="red")
        self.l67 = self.canvas.create_line(p6x,p6y,p7x,p7y,fill="red")
        self.l78 = self.canvas.create_line(p7x,p7y,p8x,p8y,fill="red")
        self.l58 = self.canvas.create_line(p5x,p5y,p8x,p8y,fill="red")

    def update(self):
        self.canvas.delete(self.l12)
        self.canvas.delete(self.l23)
        self.canvas.delete(self.l34)
        self.canvas.delete(self.l14)
        self.canvas.delete(self.l15)
        self.canvas.delete(self.l26)
        self.canvas.delete(self.l37)
        self.canvas.delete(self.l48)
        self.canvas.delete(self.l56)
        self.canvas.delete(self.l67)
        self.canvas.delete(self.l78)
        self.canvas.delete(self.l58)

        self.draw()

    def neworigin(self,origin):
        diff = [self.origin[0] - origin[0],
                self.origin[1] - origin[1],
                self.origin[2] - origin[2]]
        
        self.p1 = [self.p1[0]-diff[0],self.p1[1]-diff[1],self.p1[2]-diff[2]]
        self.p2 = [self.p2[0]-diff[0],self.p2[1]-diff[1],self.p2[2]-diff[2]]
        self.p3 = [self.p3[0]-diff[0],self.p3[1]-diff[1],self.p3[2]-diff[2]]
        self.p4 = [self.p4[0]-diff[0],self.p4[1]-diff[1],self.p4[2]-diff[2]]
        self.p5 = [self.p5[0]-diff[0],self.p5[1]-diff[1],self.p5[2]-diff[2]]
        self.p6 = [self.p6[0]-diff[0],self.p6[1]-diff[1],self.p6[2]-diff[2]]
        self.p7 = [self.p7[0]-diff[0],self.p7[1]-diff[1],self.p7[2]-diff[2]]
        self.p8 = [self.p8[0]-diff[0],self.p8[1]-diff[1],self.p8[2]-diff[2]]
        
        self.update()

    def rotate(self,axis,rad):
        x,y,z = self.origin[0],self.origin[1],self.origin[2]
        
        if axis == "x":
            
            p1y,p1z = self.p1[1]-y,self.p1[2]-z
            p2y,p2z = self.p2[1]-y,self.p2[2]-z
            p3y,p3z = self.p3[1]-y,self.p3[2]-z
            p4y,p4z = self.p4[1]-y,self.p4[2]-z
            p5y,p5z = self.p5[1]-y,self.p5[2]-z
            p6y,p6z = self.p6[1]-y,self.p6[2]-z
            p7y,p7z = self.p7[1]-y,self.p7[2]-z
            p8y,p8z = self.p8[1]-y,self.p8[2]-z

            p1y,p1z = (p1y*cos(rad))-(p1z*sin(rad)),(p1z*cos(rad))+(p1y*sin(rad))
            p2y,p2z = (p2y*cos(rad))-(p2z*sin(rad)),(p2z*cos(rad))+(p2y*sin(rad))
            p3y,p3z = (p3y*cos(rad))-(p3z*sin(rad)),(p3z*cos(rad))+(p3y*sin(rad))
            p4y,p4z = (p4y*cos(rad))-(p4z*sin(rad)),(p4z*cos(rad))+(p4y*sin(rad))
            p5y,p5z = (p5y*cos(rad))-(p5z*sin(rad)),(p5z*cos(rad))+(p5y*sin(rad))
            p6y,p6z = (p6y*cos(rad))-(p6z*sin(rad)),(p6z*cos(rad))+(p6y*sin(rad))
            p7y,p7z = (p7y*cos(rad))-(p7z*sin(rad)),(p7z*cos(rad))+(p7y*sin(rad))
            p8y,p8z = (p8y*cos(rad))-(p8z*sin(rad)),(p8z*cos(rad))+(p8y*sin(rad))
            
            self.p1[1],self.p1[2] = p1y+y,p1z+z
            self.p2[1],self.p2[2] = p2y+y,p2z+z
            self.p3[1],self.p3[2] = p3y+y,p3z+z
            self.p4[1],self.p4[2] = p4y+y,p4z+z
            self.p5[1],self.p5[2] = p5y+y,p5z+z
            self.p6[1],self.p6[2] = p6y+y,p6z+z
            self.p7[1],self.p7[2] = p7y+y,p7z+z
            self.p8[1],self.p8[2] = p8y+y,p8z+z
            
        elif axis == "y":
            
            p1x,p1z = self.p1[0]-x,self.p1[2]-z
            p2x,p2z = self.p2[0]-x,self.p2[2]-z
            p3x,p3z = self.p3[0]-x,self.p3[2]-z
            p4x,p4z = self.p4[0]-x,self.p4[2]-z
            p5x,p5z = self.p5[0]-x,self.p5[2]-z
            p6x,p6z = self.p6[0]-x,self.p6[2]-z
            p7x,p7z = self.p7[0]-x,self.p7[2]-z
            p8x,p8z = self.p8[0]-x,self.p8[2]-z

            p1x,p1z = (p1x*cos(rad))-(p1z*sin(rad)),(p1z*cos(rad))+(p1x*sin(rad))
            p2x,p2z = (p2x*cos(rad))-(p2z*sin(rad)),(p2z*cos(rad))+(p2x*sin(rad))
            p3x,p3z = (p3x*cos(rad))-(p3z*sin(rad)),(p3z*cos(rad))+(p3x*sin(rad))
            p4x,p4z = (p4x*cos(rad))-(p4z*sin(rad)),(p4z*cos(rad))+(p4x*sin(rad))
            p5x,p5z = (p5x*cos(rad))-(p5z*sin(rad)),(p5z*cos(rad))+(p5x*sin(rad))
            p6x,p6z = (p6x*cos(rad))-(p6z*sin(rad)),(p6z*cos(rad))+(p6x*sin(rad))
            p7x,p7z = (p7x*cos(rad))-(p7z*sin(rad)),(p7z*cos(rad))+(p7x*sin(rad))
            p8x,p8z = (p8x*cos(rad))-(p8z*sin(rad)),(p8z*cos(rad))+(p8x*sin(rad))

            self.p1[0],self.p1[2] = p1x+x,p1z+z
            self.p2[0],self.p2[2] = p2x+x,p2z+z
            self.p3[0],self.p3[2] = p3x+x,p3z+z
            self.p4[0],self.p4[2] = p4x+x,p4z+z
            self.p5[0],self.p5[2] = p5x+x,p5z+z
            self.p6[0],self.p6[2] = p6x+x,p6z+z
            self.p7[0],self.p7[2] = p7x+x,p7z+z
            self.p8[0],self.p8[2] = p8x+x,p8z+z
            
        elif axis == "z":
            
            p1x,p1y = self.p1[0]-x,self.p1[1]-y
            p2x,p2y = self.p2[0]-x,self.p2[1]-y
            p3x,p3y = self.p3[0]-x,self.p3[1]-y
            p4x,p4y = self.p4[0]-x,self.p4[1]-y
            p5x,p5y = self.p5[0]-x,self.p5[1]-y
            p6x,p6y = self.p6[0]-x,self.p6[1]-y
            p7x,p7y = self.p7[0]-x,self.p7[1]-y
            p8x,p8y = self.p8[0]-x,self.p8[1]-y
            
            p1x,p1y = (p1x*cos(rad))-(p1y*sin(rad)),(p1y*cos(rad))+(p1x*sin(rad))
            p2x,p2y = (p2x*cos(rad))-(p2y*sin(rad)),(p2y*cos(rad))+(p2x*sin(rad))
            p3x,p3y = (p3x*cos(rad))-(p3y*sin(rad)),(p3y*cos(rad))+(p3x*sin(rad))
            p4x,p4y = (p4x*cos(rad))-(p4y*sin(rad)),(p4y*cos(rad))+(p4x*sin(rad))
            p5x,p5y = (p5x*cos(rad))-(p5y*sin(rad)),(p5y*cos(rad))+(p5x*sin(rad))
            p6x,p6y = (p6x*cos(rad))-(p6y*sin(rad)),(p6y*cos(rad))+(p6x*sin(rad))
            p7x,p7y = (p7x*cos(rad))-(p7y*sin(rad)),(p7y*cos(rad))+(p7x*sin(rad))
            p8x,p8y = (p8x*cos(rad))-(p8y*sin(rad)),(p8y*cos(rad))+(p8x*sin(rad))
            
            self.p1[0],self.p1[1] = p1x+x,p1y+y
            self.p2[0],self.p2[1] = p2x+x,p2y+y
            self.p3[0],self.p3[1] = p3x+x,p3y+y
            self.p4[0],self.p4[1] = p4x+x,p4y+y
            self.p5[0],self.p5[1] = p5x+x,p5y+y
            self.p6[0],self.p6[1] = p6x+x,p6y+y
            self.p7[0],self.p7[1] = p7x+x,p7y+y
            self.p8[0],self.p8[1] = p8x+x,p8y+y
        self.update()
               
def go():
    x,y,z = 600,400,400
    while True:
        App.cube1.rotate("x",0.03)
        App.cube1.rotate("y",0.01)
        App.cube1.rotate("z",0.05)
        import random
        def rand():
            return random.randrange(-1,1)/10
        x += rand()
        y += rand()
        #App.cube1.neworigin([x,y,z])
        App.root.update()
        time.sleep(0.025)
    
def key(event):
    #print("Pressed",repr(event.char))
    if event.char == "x":
        App.cube1.rotate("x",0.01)
    elif event.char == "y":
        App.cube1.rotate("y",0.01)
    elif event.char == "z":
        App.cube1.rotate("z",0.01)
    elif event.char == "r":
        App.cube1.neworigin([600,400,400])
        App.root.update()
def callback(event):
    C.focus_set()
    print("Clicked at",event.x, event.y)


App = App(1200,800)

App.cube1 = Cube(App.canvas,[600,400,400],200)
App.final()
