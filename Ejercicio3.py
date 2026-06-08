#Identificadores y variables
#variables con snake_case

#Quiero obtener el nombre del alumno, ¿como debo definir mi identificador?
nombre_alumno = "Juan Dominguez"
edad_alumno = 28
promedio_final = 9.5

#Constantes con SCREAMING SNAKE CASE
TASA_IVA = 0.16
CALIFICACION_MINIMA = 7.0
PESO_PARCIAL = 0.20
PI = 3.1416
GRAVEDAD_PLANETA = 9.84
CAPACIDAD_MAXIMA_SALON = 25

#Tipado dinamico - la variable cambia de tipo
dato = 100
print(type(dato))
dato = "cien"
print(type(dato))

#Uso de constantes en un calculo
precio_base = 500.0
precio_final = precio_base * ( 1 + TASA_IVA)
print(f"Precio con IVA: ${precio_final:.3f}")

#Define 3 constantes: PESO_PARCIAL=0.20, PESO_PROYECTO=0.40 y CALIFICACION_MINIMA=6.0. Luego crea 4 variables con calificaciones y calcula el promedio usando constantes. Imprime si el aulumno aprobo o reprobo.
PESO_PARCIAL = 0.20
PESO_PROYECTO = 0.40
CALIFICACION_MINIMA = 6.0
quimica = 5
programacion = 5
matematicas = 5
español = 5 
promedio_final = (quimica + programacion + matematicas + español)/4

print(f"promedio final es:{promedio_final:.2f}")
print("Estas aprobado"if promedio_final>= CALIFICACION_MINIMA else "Estas reprobado")



      
