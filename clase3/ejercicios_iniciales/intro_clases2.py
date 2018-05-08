#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 17:06:24 2018

@author: meza
"""    

class DatosPersonales():
    def __init__(self, name, lastName):
        #print("se ejecuta al inicio")
        self.k = {##inicio del diccionario
                    'David':{
                              'lastName': 'Quispe',
                              'edad':  25,
                              'colorF': 'rojo'                            
                            },                
                    'Juan':{
                              'lastName': 'Perez',
                              'edad':  45,
                              'colorF': 'azul'                            
                            } 
                }
        self.name = name
        self.lastName = lastName
    
    def buscarNombre(self):
        kkey = self.k.keys() # ['David', 'Juan']
        if self.name in kkey:
            if self.k[self.name]['lastName'] == self.lastName:
                print("acceso correcto para {} {}".format(self.name, self.lastName))
            else:
                print("no se encontro {} {}".format(self.name, self.lastName))
        else:
            print("no existe {} {}".format(self.name, self.lastName))
    

if __name__ == "__main__":
    dq = DatosPersonales(name="David", lastName="Quispe")   #creacion del objeto
    dq.buscarNombre()
    print(dq.name)
    
    dp = DatosPersonales(name="Maria", lastName="Perez")
    dp.buscarNombre()