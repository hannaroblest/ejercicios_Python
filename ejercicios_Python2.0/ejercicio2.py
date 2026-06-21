#condicional multiple y anidada

#elif (else if) - agrega ramas intermedias

#calificador de calificaciones

nota = float(input("calificacion (0-10): "))

if nota < 0 or nota >10:
    print("calificacion invalida")
elif nota >=9.0:
    letra = "A - excelente"
elif nota >=8.0:
    letra = "B - bien"
elif nota >=7.0:
    letra = "C - suficiente"
elif nota >=6.0:
    letra = "D - aprobado minimo"
else:
    letra ="F - reprobado"

    if 0 <= nota <=10:
        print(f"nota: {nota:.1f} -> {letra}")

#Tu turno: Agrega  un mensaje que diga cuántos puntos le faltan para subir de letra. Por ejemplo, si obtuvo 7.2 (letra C), necesita 0.8 puntos para llegar a la B.

if nota >= 8.0 and nota < 9.0:
    print("te faltan", 9.0 - nota, "puntos para llegar a la A")
elif nota >= 7.0 and nota < 8.0:
    print("te faltan", 8.0 - nota, "puntos para llegar a la B")
elif nota >= 6.0 and nota < 7.0:
    print("te faltan", 7.0 - nota, "puntos para llegar a C")
elif nota < 6.0 and nota >= 0:
    print("te faltan", 6.0 - nota, "puntos para llegar a la D")

#Tu turno: Crea una condición que verifique si un año es bisiesto. Un año es bisiesto si es divisible entre 4, Y si es divisible entre 100, también debe ser divisible entre 400. Pista: usa el operador % (módulo).

año = int(input("ingresa un año: "))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("es un año bisiesto")
else:
    print("no es un año bisiesto")

#Tu turno: Reescribe el Ejercicio  usando una sola condición con and en lugar del if anidado. Luego compara las dos versiones: ¿cuál da mensajes de error más específicos y por qué?
USUARIO_CORRECTO    = "admin"
CONTRASENA_CORRECTA = "1234"

usuario = input("usuario: ")
contrasena = input("contraseña: ")

if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
    print("acceso concedido. Bienvenido.")
else:
    print("usuario o contraseña incorrectos.")