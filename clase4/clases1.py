#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:51:26 2018

@author: meza
"""

class Humano():
    def __init__(self, name=''):
        self.__name = name
        self.__edad = 10
    
    def setEdad(self, edad):
        self.__edad = edad
    
    def getEdad(self):
        return self.__edad

if __name__ == "__main__":
    obj = Humano("Moises")
    print(obj.getEdad())
    #obj.setEdad(20)
    #edad = obj.edad
    #print(edad)
    #obj.edad = 15
    #print(obj.getEdad())
    
    