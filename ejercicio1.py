#Este es un comentario de una linea

# Este es un comentario que ocupa varias lineas

"""
Este es otro ejemplo 
de comentario multlinea
"""

entero = 42 #Numeros enteros
decimal = 3.1416 #Numeros decimales (float)
logico = True #Boolean
nombre = "Juan" #String

print(type(entero))
print(type(decimal))
print(type(logico))
print(type(nombre))

#Declara variables que almacene su nombre, apellido paterno, apellido materno, edad y estatura

nombre = "Hanna Robles Tellez" #String 
edad = 18 #numeros enteros
estatura = 1.50 #numeros decimales

print(nombre)
print(edad)
print(estatura)

#list, tuple, set, dict, frozenset

nombreMateria = "Programacion"
print(nombreMateria[0])
print(nombreMateria[-1])
print(nombreMateria[0:6])

#list - mutable
calificaciones = [8.5, 9.0, 7.5, 10.0]
calificaciones.append(9.5)
calificaciones[0] = 8.0
print(calificaciones)

#tuple - inmutable
coordenadas = (19.4326, -99.1332)
print(coordenadas[0])

#dict - clave:valor 
alumno = {"nombre" : "Hanna", "edad": 18, "promedio": 9.4 }
print(alumno["nombre"])
alumno["promedio"] = 9.6
print 