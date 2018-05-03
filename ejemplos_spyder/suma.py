#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 16:35:52 2018

@author: meza
"""

def sumar(x,y):# x,y parametos
    rr=x+y
    return rr
###############################
def pares(ini=0,top=0):
    l=[]
    for i in range(ini,top+1):
        if(i%2==0):
            l.append(i)
    return l
################################

r = sumar(3,4)#3,4 argumentos
print(r)

rrr = pares(top=45)
print(rrr)



