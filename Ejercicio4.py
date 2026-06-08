#Palabras reservadas de Python

#Son identificadores que tienen un significado especial en el lenguaje de programacion Python. Estas palabras no pueden ser utilizadas como nosmbres de variables, funciones,clases u otros identificadores, ya que estan reservadas para uso interno de lenguaje . Algunas de las palabras reservadas mas comunes en Python incluyen:

#Estructuras de control
#if,else,elif,while,for,break,continue,pass,with

#Definicion de estructuras
#def,class,return,import,from,as,try,except,finally,raise,global,nonlocal

#Valores y operadores logicos
#True,False,None,and,or,not,is,in,assert,del,rraise

#funciones de entrada y salida
#ENTRADA:input()
#SALIDA: print()

nombre = input("¿Cual es tu nombre?")
edad = int(input("¿Cual es tu edad?"))

#diferentes formas de imprimir

print("hola" + nombre)#con coma
print("hola", nombre)#con concatenacion
print(f"hola{nombre},tienes{edad}años")#con f-strings
