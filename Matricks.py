import matplotlib.pyplot as plt
import math
import numpy as np
import cmath



class Printer:

    def __init__(self, campo, vel_linear, vel_angular):
       self.e = float(1.6*math.pow(10, -19))
       self.m = float(9*math.pow(10, -31))
       self.c = float(campo)
       self.v = float(vel_linear)
       self.w = float(vel_angular)
    pass

'''    def Plot(self):
        dif = self.max - self.min

        y = np.zeros(dif*100)
        x = np.linspace(self.min, self.max , dif*100)

        for i in range(0, dif*100):

    # HERE YOU PUT THE FORMULA#
    #x[i] is the x of the math function#

            y[i] = 50*x[i]
        return plt.plot(x,y)

    def Config(self):
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

    def Show(self):
        Graph(self.min, self.max, self.title, self.xlabel, self.ylabel).Plot()
        Graph(self.min, self.max,  self.title, self.xlabel, self.ylabel).Config()
        plt.show()
'''
