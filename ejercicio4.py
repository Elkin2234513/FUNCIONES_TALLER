# Construir una función que reciba como parámetro una lista de datos numéricos y que retorne el promedio de dichos datos.

print("--------------------------------")
print("---- PROMEDIO LISTA DATOS ------")
print("--------------------------------")

#Definición de la función
def calcula_promedio_lista(lista):
    suma = sum(lista) 
    promedio = suma / len(lista) 
    print("El promedio de la lista es:",promedio)


#Entrada
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Procesamiento
calcula_promedio_lista(lista)

#Salida
print("\nEso era...")