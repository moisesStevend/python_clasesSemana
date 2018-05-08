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

#pi = 3.14159265359
pi = round(math.pi,6)
E = 0.000001
pi_p = round(pi - E,6)
print("pi pedido: ")
print("0.000001")
print(pi_p)

num = 4
den = 1
serie = 0
veces = 500000
count = 0
cambS = 1

while(True):
    serie += (num/den)*(cambS)
    if round(pi - round(serie,6),6) == E:
        break    
    den+=2
    cambS=cambS*(-1)   

print(serie)
