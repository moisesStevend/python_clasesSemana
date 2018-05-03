#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 17:52:21 2018

@author: meza
"""

#lista de listas
l=[3,4,5]
l1=['hola',5, 6.7, True, [4,5,6]]

l2=[[4,5],[6,7],[5,78]]

for i in l2:
    print(i)
    
max(l)

#funcion map
dd = lambda x: x*2
ll = [3,4,5,7]
m = map(dd, ll) #map(funcion, lista)  generador


#generadores
def mi_generador(*args):#(1,4,5,6,7)
    for i in args:
        yield i*2
    

for i in mi_generador(1,4,5,6,7):
    print(i)























