#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:37:50 2018

@author: meza
"""

class Operaciones():
    def sumar(self, x,y):
        return x+y
    
    def restar(self, x,y):
        return x-y
    
    def multiplicar(self, x,y):
        return x*y

if __name__=="__main__":
    op = Operaciones()
    r = op.sumar(4,5)
    print(r)
    