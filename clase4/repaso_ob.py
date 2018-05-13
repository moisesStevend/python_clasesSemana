#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 15:13:58 2018

@author: meza
"""
class Humano():
    def __init__(self, re): #re:rango de edad
        self.re = re     # self.re : atributos de la clase  
    
    def __hablar(self, text='hola', inv=False):
        def invertir(text): #funcion dentro de un metodo
            return text[::-1] #invierta el texto
        
        if inv==True:   #flag para invertir
            text = invertir(text)      
        return text
    
    def __pensar(self, veces=1):
        print("estoy pensando!"*veces)
    
    def opinar(self, text):
        self.__pensar()
        ht = self.__hablar(text)
        return ht 

if __name__=="__main__":
    rango = range(12,20)
    moi = Humano(re=rango) #llama al metodo init
    mo = moi.opinar("debo pensar primero")
    print(mo)
    #print(list(moi.re))
    #mh = moi.hablar(text="labotec", inv=True)
    #print(mh)
    


