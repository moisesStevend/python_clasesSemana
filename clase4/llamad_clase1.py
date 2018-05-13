#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:06:21 2018

@author: meza
"""

import clases1

class Otro():
    pass

if __name__ == "__main__":
    obj_d = clases1.Humano("David")
    obj_j = clases1.Humano("Juan")
    
    obj_d.setEdad(40)
    obj_j.setEdad(25)
    
    edad_d = obj_d.getEdad()
    edad_j = obj_j.getEdad()
    
    print("edad David",edad_d)
    print("edad Juan",edad_j)
