#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 16:11:28 2018

@author: meza
"""
#numeros pares en python
#l=[1,2,3,4,5,6,7,8,9,10]
inicio=2
tope=10
ll=range(inicio, tope+1)

for i in ll:
    if i%2==0:
        print(i)

m = [i for i in range(2,11) if (i%2==0)]
print(m)

#while
ll=range(inicio, tope+1)
i=0
while i!=len(ll):
    if ll[i]%2==0:
        print(ll[i]) #es par
    i+=1



















