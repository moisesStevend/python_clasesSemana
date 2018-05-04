#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 14:28:38 2018

@author: meza
"""
__version__ = "Produccion"

#Buscar un valor
#class Bsuqueda():
def busca_valor(ll, vv):#lista a recorrer, valor de bus
    try:
        if len(ll)==0:#es vacio
            print("Vector vacio")
            return False
        
        #acces=False
        for i in ll:
            if i==vv:
                return True
                #acces=True
                #print(acces)
        #if acces!=True:
        return False
        #    print(False)
    except:
        return False
#buscar el indice
def busca_pos(ll, vv):   
    #f=busca_valor(ll,vv)
    #print("conocer valor de func: ",f, type(f))
    if (busca_valor(ll,vv)==False):
        print("no se encontro el valor en el vector")
        return False 
    #if (busca_valor(ll,vv)==None):
    #    return False 
    #print("se encontro el valor en el vector")
    index=0
    for i in ll:
        if vv==i:
            #print("Verdad, posición E [0, dx-1] y es: {}".format(index))
            #s="Verdad, posición E [0,{}] y es: {}".format(len(ll)-1,index)
            return index#, s
        index+=1        

if __name__ == "__main__":
    l=[2,3,4,7,8]
    v=2
    
    s = busca_pos(l,v)
    print(s)
