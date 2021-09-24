from _typeshed import Self
import matplotlib.pyplot as plt
import math
import numpy as np

class Impressora:

    def __init__(self, campo, vel_linear, vel_angular, tempo_0):
       self.e = float(1.6*math.pow(10, -19))
       self.m = float(9*math.pow(10, -31))
       self.c = float(campo)
       self.v = float(vel_linear)
       self.w = float(vel_angular)
       self.t = float(tempo_0)
    pass

    def Raio(self, tempo):
        return (self.e*self.c*math.pow(tempo, 2)) / (2*self.m)

    def eixoX(self, tempo):
        return self.Raio(tempo)*math.sin(self.w*tempo)

    def eixoY(self, tempo):
        return self.Raio(tempo)*math.cos(self.w*tempo)

