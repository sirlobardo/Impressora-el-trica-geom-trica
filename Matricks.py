import matplotlib.pyplot as plt
import math
import numpy as np
import cmath

class Bhaskara:
    def __init__(self, A, B, C):
        self.a = float(A)
        self.b = float(B)
        self.c = float(C)
    pass

    def delta(self):
        return self.b**2 - 4*self.a*self.c
    
    def raiz1(self):
        return (- b + cmath.sqrt(Bhaskara(self.a, self.b, self.c).delta())) / (2*self.a)

    def raiz2(self):
        return (- b - cmath.sqrt(Bhaskara(self.a, self.b, self.c).delta())) / (2*self.a)
        
        
