#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:56:37 2018

@author: meza
"""
class Operaciones():   #creacion de la clase
    def __init__(self):  #metodo init, sirve para ejecutar al inicio
        self.f = 40     #variable de la clase
    
    def test(self):  #metodo
        print(self.f)
        
    def test_edit(self, nw): #metodo (self,)
        self.f = nw
        self.test()
    
    def suma(self, a,b,c, *k, **kw):
        print(a,b,c)
        print("tipo de k: {}".format(type(k)))
        print("valor de k: {}".format(k))
        
        print("tipo de kw: {}".format(type(kw)))
        print("valor de kw: {}".format(kw))
        #print(type(kw))
    
    def resta(self, a,b,c,d, *k):#a,b,c,d,k : parametros
        for i in k:
            print(i, end=',')
        print('\n')

if __name__ == "__main__":  #operacion de ejecucion solo en el script
    op = Operaciones()   #creamos un objeto
    op.test_edit(12)     #accedemos al metodo
    #op.test()
    #op.suma(4,5, 1,2,3,7,9, h=34,y=67)
    op.resta(4,5,6,7, 4,4,3,2) #3,5,6,7,4,4,3,2 : argumentos
    #op.test()

