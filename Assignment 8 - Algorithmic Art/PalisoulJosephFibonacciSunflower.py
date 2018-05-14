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
import math
from tkinter import *

class Fibonacci():
    def s5(self, n, r): # works better for first direction
        spirals = []
        for i in range(n+1):
            spirals.append(((r*(i**0.5),((i*(360)/(((5**0.5)+1)/2))%360))))
        return spirals

    def pol2cart(self, r, theta):
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        return x,y

    def calculate_coordinates(self, num_points = 200, distance = 15):
        # do the cartesian conversion
        self.coordinates = [self.pol2cart(r, t) for r, t in self.s5(num_points, distance)]

        # center for the canvas
        self.coordinates = [(x+250,y+250) for x, y in self.coordinates]

    def plot_numbers(self, canvas):
        h = 1
        self.calculate_coordinates(num_points = 200, distance = 15)
##        for x, y in self.coordinates:
##            canvas.create_oval(x+7, y+7, x-7, y-7)
##            canvas.create_text(x, y, text = h)
##            h += 1

    def plot_lines(self, canvas):
        for delta in [21, 34]:
            for start in range(34):
                x0, y0 = self.coordinates[start]
                print (x0, y0)
                i = start + delta
                while i < len(self.coordinates):
                    x1, y1 = self.coordinates[i]
                    canvas.create_line(x0, y0, x1, y1)
                    x0 = x1; y0 = y1
                    i += delta

    def create_gui(self):
        master = Tk()
        canvas = Canvas(master, width = 1000, height = 1000)
        canvas.pack()

        self.plot_numbers(canvas)
        self.plot_lines(canvas)

        mainloop()


def main():
    f = Fibonacci()
    f.create_gui()
    return 0

if __name__ == '__main__':
    main()
