# Construir una función que reciba como parámetro una lista de datos numéricos y retorne el promedio de los datos pares.

print("--------------------------------")
print("-- PROMEDIO PARES LISTA DATOS --")
print("--------------------------------")

#Definición de la función
def calcular_promedio_pares_lista(lista):
    suma_pares = 0
    cantidad_pares = 0
    
    for num in lista:
        if num % 2 == 0:
            suma_pares += num
            cantidad_pares += 1
    
    if cantidad_pares > 0:
        promedio = suma_pares / cantidad_pares
        print(promedio)
        return promedio
    else:
        return None

#Entrada
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Procesamiento
promedio = calcular_promedio_pares_lista(lista)
if promedio is not None:
    print(f"El promedio de los datos pares es {promedio}")
else:
    print("No hay datos pares en la lista.")

#Salida
print("\nEso era...")