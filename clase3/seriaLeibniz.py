#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 18:43:39 2018
Aproximar al valor Pi, 
Leibniz:    4/1 - 4/3 + 4/5 - 4/7  + 4/9 - 4/11 + ......

num = 4

@author: meza
"""
import math 

class SerieLeibniz():
    def __init__(self, redondeo=6, E=0.000001):
        self.email = "moises.stevend@gmail.com"
        self.pi = round(math.pi,redondeo)
        self.E = E 
        self.pi_p = round(self.pi - self.E,6)

        self.num = 4
        self.den = 1
        self.serie = 0
        self.cambS = 1

    def calculo(self):
        while(True):
            self.serie += (self.num/self.den)*(self.cambS)
            if round(self.pi - round(self.serie,6),6) == self.E:
                break    
            self.den+=2
            self.cambS*=(-1)   
        
        return self.serie

if __name__ == "__main__":
    nE = input("ingrese aproximacion: ")
    s1 = SerieLeibniz(E=float(nE), redondeo=len(nE)-2)
    rs1 = s1.calculo()
    print(rs1)
