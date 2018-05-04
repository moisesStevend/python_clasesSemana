#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:11:53 2018

@author: meza
"""

tam = int(input("*) tamano de vector: "))
count=0
l=[]
while count<tam:
    r=int(input("\t >ingrese valor {}: ".format(count+1)))
    l.append(r)
    count+=1

print("\nla lista es : {}".format(l))

#l=[5,6,8,9,9,5]
l2=[]
d={}

x=0
global j

while x<len(l):
    j=0
    init=l[x]  #init: cada valor de la lista
    for i in l: #recorres la lista 
        if init==i:#preguntes si init se repite
            j+=1  #la veces q se repite
    if j==1:    # si solo se repite una vez
        l2.append(init)  #agregas a la nueva lista
    #d[init]=j
     #variables auxiliares
    x+=1 #variables auxiliares

print("j: ",j)
print("la nueva lista es: {}".format(l2))







    

