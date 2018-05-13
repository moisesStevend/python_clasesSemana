#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:15:14 2018

@author: meza
"""
class Matriz():
    def __init__(self,n, m ):
        self.n = n
        self.m = m
                    #n=2, m=3
    def crearMatriz(self):
        mat=[]
        
        for i in range(self.n):
            f=[0]*self.m  #[0,0,0]
            mat.append(f)
        
        return mat
    
    def leerMatriz(self):
        x=self.crearMatriz()
        
        for i in range(self.n):
            for j in range(self.m):
                val=input("ingrese [{}][{}]: ".format(i,j))
                x[i][j]=int(val)
        
        return x
    
    def mostrarMatriz(self, mx):
        f = len(mx)  #tamano de filas
        c = len(mx[0]) #tamano de columnas
        
        for i in range(f):
            for j in range(c):
                val=mx[i][j]
                print(val,"",end="")
            print()
    def copiarMatriz(self,mx):
        cmx=[]
        for f in mx:
            cmx.append(f[:])
        return(cmx)
        
    def sumarFilas(self,mx):
        f=len(mx)
        c=len(mx[0])
        sf=0
        for i in range(f):
            for j in range(c):
                val=mx[i][j]
                sf=sf+val
        print("%d suma fila (%d) "% (sf,i))
        return sf
    
if __name__ == "__main__":
    #variables iniciales
    fila=2
    columna=3
    #crea objeto
    print("Matriz de fila {} y columan {}".format(fila,columna))
    mat = Matriz(fila,columna) 
    x = mat.leerMatriz()
    sfx = mat.sumarFilas(x)
    
    #print("\nmatrix resultante: ",x)
    #print("\n\n")
    #mat.mostrarMatriz(x)
    #crea matriz de 3x4
    #cmat = mat.crearMatriz(fila,columna)
    #print(cmat)
    