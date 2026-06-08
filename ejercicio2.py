# - Casting basico
# Implicita: int + float = float automaticamente
resultado = 5 + 2.0
print(resultado)
print(type(resultado))

#Emplicita: str a int
texto_numero = "42"
numero_real = int(texto_numero)
print(numero_real + 8)

#Explicita: int a str para concatenar

edad = 28
mensaje = "Hola, soy Juan y mi edad es " + str(edad)
print(mensaje)

#float a int
precio = 9.99
print(int(precio))

numero = 7.35
redondeado = round(numero)
print(redondeado) 

# Simularemos input con variables fijas
dato_usuario = "25"
print(type(dato_usuario))
#print(dato_usuario + 5)

edad_correcta = int(dato_usuario)
print(edad_correcta + 5)

#Patron correcto para entrada de datos:
##edad = int(input("ingresa tu edad"))

#Escribe un programa que pida al usuario su nombre (str) y su año de nacimiento (int). Calcula e imprime su edad aproximada restando al año actual (2026).
nombre = (input("ingresa tu nombre"))
año_nacimiento = int(input("ingresa tu año"))
print(2026-año_nacimiento)
