# Payton usa la sangria (espacios al inicio de la linea) para delimitar bloques de codigo.{}, Pyton usa 4 espacios por nivel. Esta es la diferenci visual mas importante entre python y otros lenguajes.

#if condicion:
#    instruccion1
#else:
#    instruccion2

#Toda estructura de control termina su primera linea con dos puntos ":". Los dos puntos le dicen a python: el bloque de esta estructura comienza en la siguiente linea. si se omiten, Python genera SyntaxError: expected ":"

#= asignar un valor
#== comparar dos valores iguales que 
#!= diferente de 
#> mayor que / >= mayor o igual
#< menor que / <= menor o igual
# and ambas condiciones True / or Al menos de una es true / not negacion logica

#IF ejecuta un bloque unicamente si la condicion es True. si la condicion es False, el bloque se salta por completo y el programa continua. Solo tiene una rama posible

#SI condicion ENTONCES
#    Instruccion
#FIN SI


nota = 8.5

if nota >=6.0:
 print("el alumno aprobo")

print("fin del programa")

#CONDICIONAL DOBLE - IF/ELSE
#El else garantiza que SIEMPRE se ejecuta algo. Sin importar si la condicion es True o False, el programa toma uno de los dps caminos.

CALIFICACION_MINIMA = 7.0

nota = float(input("ingresa tu calificacion"))

if nota >= CALIFICACION_MINIMA:
  print(f"aprobado con{nota:.1f}")
else:
 print(f"reprobado con{nota:.1f}")
 faltaron =CALIFICACION_MINIMA - nota
 print(f"te faltaron{faltaron:.1f}puntos para aprobar")


#condiciones compuestas and / or en accion 

edad = int(input("tu edad: "))
tiene_ine = input("¿tiene ine (si/no): ")

if edad >= 18 and tiene_ine == "si":
    print("si puedes votar aun")

#validacion de rango con "and" y "or"
calificacion = float(input("calificacion (o-10)"))

if calificacion <0 or calificacion >10:
    print("calificacion fuera de rango")
else:
    print(f"calificacion registrada: {calificacion:.1f}")

