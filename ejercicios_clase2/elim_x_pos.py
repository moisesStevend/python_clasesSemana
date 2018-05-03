#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 17:11:48 2018

@author: meza
Especifique e implemente un sub programa 
para eliminar un elemento por posicion.
"""

def existe_pos(l,p):
    tam=len(l)-1  #4
    if p>tam:
        print("fuera de rango")
        return False
    return True

def elimin_pos(l,p):
    if existe_pos(l,p)==False:
        return False
    
    l2=[]
    for i in l:
        if l[p]==i: #posicon a borrar " "
            continue #retorna a la siguiente iteracion del for
        l2.append(i)
        
    return l2

if __name__=="__main__":
    l=[6,73,4,55,90]
    pos=0
    print("l:",l, "pos a cambiar l[4]",l[pos])
    
    l2 = elimin_pos(l,pos)
    print("nuevo l:",l2)

