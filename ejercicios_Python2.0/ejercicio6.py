#SISTEMA DE GRABACION DE CALIFICACIONES

#Una escuela necesita un programa que registre las calificaciones de 15 estudiantes, calcula los resultados del grupo y genera un informe final en la pantalla 
#nota minima de aprobacion 6.0, en numero de estudiantes a ingresar: 15, el programa debe rechazar cualquier calificacion fuera del rango de 0.0 a 10.0 y solicitar al usuario de nuevo hasta que se intriduzca un valor valido 

#constantes 
calificacion_aprobatoria = 6.0
numero_estudiantes = 15

nombres = []
calificaciones = []

for i in range (numero_estudiantes):
    print("\nestudiante", i + 1)
    nombre = input("ingresa el nombre del estudiante: ")
    calificacion = float(input("ingresa la calificacion: "))

    while calificacion < 0.0 or calificacion > 10.0:
        print("error, la calificacion debe estar entre 0 y 10")
        calificacion = float(input("ingresa nuevamente la calificacion: "))

    nombres.append(nombre)
    calificaciones.append(calificacion)

suma_calificaciones = 0
aprobados = 0
reprobados = 0

mayor_calificacion = calificaciones[0]
menor_calificacion = calificaciones[0]

nombre_mayor = nombres[0]
nombre_menor = nombres[0]

for i in range(numero_estudiantes):
    suma_calificaciones = suma_calificaciones + calificaciones[i]

    if calificaciones[i] >= calificacion_aprobatoria:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
    if calificaciones[i] > mayor_calificacion:
        mayor_calificacion = calificaciones[i]
        nombre_mayor  = nombres[i]
    if calificaciones[i] < menor_calificacion:
        menor_calificacion = calificaciones[i]
        nombre_menor = nombres[i]

promedio = suma_calificaciones / numero_estudiantes
porcentaje_aprobados = (aprobados / numero_estudiantes) * 100

print("------------------------------------------------------------------")
print("    nombre    calificacion    estado   letra")
print("---------------------------------------------------------------------")

for i in range(numero_estudiantes):
    if calificaciones[i] >= calificacion_aprobatoria:
        estado = "aprobado"
    else:
        estado = "reprobado"
    if calificaciones[i] >= 9.0:
        letra = "A"
    if calificaciones[i] >= 8.0:
        letra = "B"
    if calificaciones[i] >= 7.0:
        letra = "C"
    if calificaciones[i] >= 6.0:
        letra = "D"
    else:
        letra = "F"


    print(f"{nombres[i]} {calificaciones[i]} {estado} {letra}")
print("------------------------------------------------------------------------")

print(f"prmedio del grupo: {promedio:.1f}")
print(f"total de aprobados: {aprobados}")
print(f"total de reprobados: {reprobados}")

print("nestudiante con la mayor calificacion: ")
print(f"{nombre_mayor} - {mayor_calificacion}")

print("/nestudiante con la menor calificacion: ")
print(f"{nombre_menor} - {menor_calificacion}")

print(f"/nporcentaje de aprobados: {porcentaje_aprobados:.1f}%")