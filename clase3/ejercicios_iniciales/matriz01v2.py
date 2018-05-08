#
# nomPrograma: vector01v2.py
# descripcion: Operaciones basicas de MATRICES
# Sea m la metriz de enteros:
#      | 2,  9,   3 |
#  m = | 1, -5   11 |
#      | 0,  1   -1 |
#  m = [[2,9,3][1,-5,11][0,1,-1]]
#  col = [0,0,0]
#  fil = 3
#    m = col*fil=[[0,0,0][0,0,0][0,0,0]]
#  Tambien puede hacer con range. Veamos el programa un poco mas formal
#  pasando parametros
#               manual de Usuario
#   a. Ejecute el programa
#   b. Primero debe crear la matriz que desea
#   c. Luego leer para cargar la matriz con sus elementos 
#   d. Luego debe realizar las operaciones que desea
#
#       TAREA
#   1. Analice y ejecute.
#   2. Analice la estructura de los modulos (porque esos modulos)
#   3. Analice el funcionamiento de cada uno de los modulos
#   4. Implemente operaciones especificadas de las operaciones buscar,
#      editar un dato, mostrar una fila o columna determinada
#   5. Implemente la suma de matrices
#   6. Implemente la multiplicacion de matrices
#
# Autor: GASA
# Fecha: 01052018
#

import sys
def crearMatriz():
    # Rutina de creacion
    nfil=int(input("Numero de filas   :  "))
    ncol=int(input("Numero de Columnas:  "))
    m=[]
    #Separa/crea espacio en la RAM para la matriz
    for i in range(nfil):
        m.append([0]*ncol)

    print("La MATRIZ ha sido creada...")
    return(m)   

def leerMatriz(x):
    #Rutina de Lectura
    for i in range(len(x)):
        for j in range(len(x[i])):
            #print(, end="")
            dato=int(input("Ingrese dato: [{}],[{}]: ".format(i,j)))
            x[i][j]=dato
    return (x)

def mostrarMatriz(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            elem=x[i][j]
            print(elem,"",end="")
            #print(elem, '',end="")
        print("")

#ACCION buscarDato(x, dato)
#Busca dato en la matriz x
#PRE: x=<> o x=<<1,1, ...1> <2,2,...2>...<...>> dato pertenece a x
#POS: matriz vacia o dato no se encuentra o dato esta fila i, columna j
def buscarDato(x, dato):
    hallado=False
    dxf=len(x)
    dxc=len(x[0])

    if(dxf>0 and dxc>0):
        for i in range(len(x)):
            for j in range(len(x[0])):
                elem=x[i][j]
                if(elem==dato):
                    pf=i
                    pc=j
                    hallado=True
                    break
        if(hallado==True):
            print(dato, " encontrado en fila: ",pf+1,"columna: ", pc+1)
        else:
            print(dato, " No encontrado....")


#ACCION editarDato(x, dato)    
#Busca dato en la matriz x y lo edita o modifica (debe utilizar un modulo
# buscar que retorna la posicion  del elemento a editar)
#PRE: x=<> o x=<<1,1, ...1> <2,2,...2>...<...>> dato pertenece a x
#POS: matriz vacia o dato no se encuentra o dato ha sido modificado
#     (debe dar evidencia de la moficacion de la matriz modificada)
def editarDato(x, dato):
    x=[]


#ACCION sumaMatrices(x, y)
#Suma la matriz x e y y retorna la matriz suma z
#PRE: x=<> o x=<<1,1, ...1> <2,2,...2>...<...>> 
#     y=<> o y=<<1,1, ...1> <2,2,...2>...<...>> / x, y tiene dim=[n,m]
#POS: matriz vacia o matriz z que es la suma de los elementos de x mas y
def sumaMatrices(x, y):
    x=[]

    
#ACCION productoMatrices(x, y)
#Suma la matriz x e y y retorna la matriz suma z
#PRE: x=<> o x=<<1,1, ...1> <2,2,...2>...<...>> 
#     y=<> o y=<<1,1, ...1> <2,2,...2>...<...>>
#     / x dim=[n,m] y x dim=[m,n1] 
#POS: matriz vacia o matriz z que es el producto los elementos de x mas y
def productoMatrices(x, y):
    x=[]

def menu():
    opc=-1
    while(opc<0 or opc>4):
        print("M A T R I Z \n")
        print("0. TERMINAR ")
        print("1. Crear Matriz ")
        print("2. Leer Matriz ")
        print("3. Mostrar  ")
        print("4. Buscar dato  ")
        #print(,end="")
        opc=int(input("Digite su opcion: "))
    return opc

def operacionesMatriz():
    opc=menu()
    a=[]
    while(opc!=5):
        if(opc==0):
            print("El programa ha terminado...")
            sys.exit(0)
        elif(opc==1):
            a=crearMatriz()
        elif(opc==2):
            a=leerMatriz(a)
        elif(opc==3):
            mostrarMatriz(a)
        else:
            dat=int(input("Ingrese dato a buscar: "))
            buscarDato(a,dat)
        opc=menu();
        
operacionesMatriz()
    
