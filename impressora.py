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

    def eixoX(self, tempo):
        return self.Raio(tempo)*math.sin(self.w*tempo)

    def eixoY(self, tempo):
        return self.Raio(tempo)*math.cos(self.w*tempo)

    def interT(self):
        #te = self.com / self.v
        #for i in range(0, self.el+1, 1):
            #t = te*i
        te = self.com / self.v
        tf = self.el * te
        t = np.linspace(te, tf, self.el)
        return t 

