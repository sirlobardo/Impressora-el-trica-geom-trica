import matplotlib.pyplot as plt
import math
import numpy as np

class Impressora:

    def __init__(self, campo, vel_linear, vel_angular, n_ele, comp_barra):
       self.e = float(1.6*math.pow(10, -19))
       self.m = float(9*math.pow(10, -31))
       self.c = float(campo)
       self.v = float(vel_linear)
       self.w = float(vel_angular)
       self.el = int(n_ele)
       self.com = float(comp_barra)
    pass

    def Raio(self, tempo):
        return (self.e*self.c*math.pow(tempo, 2)) / (2*self.m)

    def eixoX(self, tempo, theta):
        return self.Raio(tempo)*math.sin(theta)

    def eixoY(self, tempo, theta):
        return self.Raio(tempo)*math.cos(theta)
    def Theta(self):
        thetai = 2 * math.pi / self.el
        return np.linspace(thetai, 2*math.pi, self.el)
    def interT(self):
        te = self.com / self.v
        tf = self.el * te
        t = np.linspace(te, tf, self.el)
        return t
    def Graph(self, eixoX, eixoY, tempo):
        plt.title("Impressora de Elétrons")
        plt.xlabel("Eixo X")
        plt.ylabel("Eixo Y")
        y = np.empty(self.el)
        x = np.empty(self.el)
        plt.plot(x,y)
        return plt.show()
        


