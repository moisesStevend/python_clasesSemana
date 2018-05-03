#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:39:48 2018

@author: meza
Implemente en lenguaje Python la siguiente especificacion editar un dato reutilizando las
operaciones buscar e insertar por posicion. Mmmmm
ACCION editarxValor(Vector x, ENTERO dx, ENTERO dato)
//Edita el elemento dato del vector x
//PRE: x = < >  x = <e 1 , e 2 ...,e n >  dato  [e 1 , e n ]
//POS: X = <e 1 , e 2 ,... ne i , ..., e n > / ne i es el nuevo dato editado o modificado.
"""
import busqueda_valores as vb

def xinsert(lt, pos, nw):#[4,5,6], 4
    try:
        if vb.busca_valor(lt,lt[pos])==False:
            return False
    except:
        return False
    lt[pos]=nw
    return lt

if __name__ == "__main__":
    l=[7,84,2,38,4,5,7]
    new_pos=3
    new_valor=100
    
    if xinsert(lt=l, pos=new_pos, nw=new_valor)!=False:
        print("de lista {}, se cambia la pos {} por {}".format(l,new_pos,new_valor))
        lr = xinsert(lt=l, pos=new_pos, nw=new_valor)
        print("nuevo l:",lr)
    