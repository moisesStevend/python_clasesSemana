#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 17:01:14 2018

@author: meza

"""
v=[4,5,6,7,4,2]
#hallar los numeros pares
for i in range(len(v)):#  for i in [0,1,2,3,4,5]:
    val=v[i]
    if (val % 2 == 0 ):
        print(v[i], end='')

print()
#reverso de la lista
for i in range(-1,(-len(v)-1),-1):# [-1, -2, -3, -4, -5, -6]
    val=v[i]
    print(val, end=' ')