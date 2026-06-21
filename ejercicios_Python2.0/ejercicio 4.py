#CICLO WHILE - Repite un bloque MIENTRAS una condición sea True. Se usa cuando NO sabes de antemano cuántas veces necesitas 
# repetir - el número de repeticiones depende de lo que ocurra durante la ejecución

#Regla crítica: algo dentro del while DEBE cambiar en cada iteración para que la condición eventualmente sea False. 
# Sin eso, el ciclo nunca termina.

#Ejercicio - while básico: contador y acumulador

N = int(input("Suma del 1 hasta: "))
i = 1 #Contador - empieza en 1
suma = 0 #Acumulador - empieza en 0

while i <= N:
    suma = suma + i
    i = i + 1 

print(f"Suma de 1 a {N}: {suma}")

#Verificación matemática: N*(N+1)/2
formula = N * (N +1) //2 
print(f"Verificación con fórmula: {formula}")

#Tu turno: Reescribe el ejercicio usando for en lugar de while. ¿Cuál versión es más natural para este problema? 
# Explica por qué con tus palabras.

N = int(input("suma del 1 hasta: "))
sima = 0

for i in range(1, N + 1):
    suma= suma + i 

print(f"suma de 1 a {N}: {suma}")

formula = N * (N + 1) //2
print(f"verificacion con formula: {formula}")

#el for es mas natural facil porque sabes cuantas veces vas a repetir desde 1 hasta N 
#el while es mejor cuando no sabes cuantas veces a repetir 

#Ejercicio - while para validar entrada: el patrón de reintento.

nota = float(input("Calificación (0-10):"))

while nota < 0 or nota > 10:
    print("Calificación inválida. Debe ser entre 0 y 10.")
    nota = float(input("Calificación (0-10)"))

print(f"Calificación registrada: {nota:.1f}")
print()

#While True + break
while True:
    edad = int(input("Tu edad(1-80):"))
    if 1 <= edad <=80:
        break
    print("Edad inválida, intenta de nuevo.")

print(f"Edad registrada: {edad}")

#Tu turno: Crea un programa que pida al usuario adivinar un número secreto (define tú el número con una constante). 
# Con while, sigue pidiendo hasta que lo adivine e imprime cuántos intentos necesitó.

numero_secreto = 7
intentos = 0

print("¡adivina el numero secreto! (entre 1 y 20)")

while True:
    numero = int(input("tu numero: "))
    intentos = intentos + 1

    if numero == numero_secreto:
        break
    print("incorrecto, intenta de nuevo")

print(f"¡lo adivinaste!era el {numero_secreto}")
print(f"necesitaste {intentos} intento(s)")


