#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:51:54 2018

@author: meza
Implemente en lenguaje Python la siguiente especificacion buscar la posicion de un
deteminado elemento.
ACCION buscarDato1(Vector x, ENTERO dx, ENTERO dato)
//Busca el elemento dato y retorna la posición que ocupa 
//o debe ocupar en el vector x
//PRE: x = < >  x = <e 1 , e 2 ...,e n > / e 1 < e 2 < ...,<e n  dato  x[ ]
//POS: Si dato <= e 1 → pos=0  Si dato >= e 1 → pos=dx  Si dato  [e 1 , e n ] pos  <0, dx>
"""

import busqueda_valores as bv

def ord_lista(ll):#[3,9,5,1]
   #asumimos que es el minimo
    l2=[]       #lista ordenada
    count=0
    
    while count<4:
        #print("ll al inicio del while: ",ll)
        mini=ll[0] 
        for i in ll:#[3,9,5]
            if i<mini:
                mini=i
        #print("mini:",mini)     
        l2.append(mini)  #[1]
        #print("l2: ",l2)
        ll.remove(mini)   #[3,9,5]
        #print("nuevo ll:",ll)
        count+=1
    
    return l2#lista ordenada

if __name__ == "__main__":
    l=[2,78,9,92]  #[2,9,78,92]
    v=9
    
    if bv.busca_valor(l,v)==True:
        r = bv.busca_pos(l,v)
        print("la posicion de {} en {} es: {}".format(v,l,r))
        
        ro = ord_lista(l)
        rr = bv.busca_pos(ro,v)
        print("la posicion de {} en {} es: {}".format(v,ro,rr))
    
    