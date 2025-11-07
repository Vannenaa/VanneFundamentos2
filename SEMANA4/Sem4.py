print("\nEjercicio 1: Tabla de multiplicar")

numero = 5
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


print("\nEjercicio 2: Suma de lista")
numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num
print(f"La suma total es: {suma}")


print("\nEjercicio 3: Contar vocales en un texto")
texto = "Alo, que haciendo mi gente en miercoles"
contador = 0
for letra in texto:
    if letra.lower() in "aeiou":
        contador += 1
print(f"Hay {contador} vocales")


print("\nEjercicio 4: Número mayor en la lista")
numeros = [15, 42, 8, 23, 67, 31]
mayor = numeros[0]  # Empezamos con el primero de la lista
for num in numeros:
    if num > mayor:
        mayor = num
print(f"El número mayor es: {mayor}")


print("\nEjercicio 5: Lista de cuadrados del 1 al 5")
cuadrados = []
for a in range(1, 6):
    cuadrados.append(a ** 2)
print(cuadrados)
