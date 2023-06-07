# Construir una función que reciba como parámetro una lista de datos numéricos y retorne la suma de dichos datos.

print("--------------------------------")
print("-------- SUMA LISTA DATOS ------")
print("--------------------------------")

#Definición de la función
def sumar_lista_datos(lista):
    suma = 0
    for dato in lista:
        suma += dato
    print("La suma de la lista es:",suma)



#Entrada
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Procesamiento
sumar_lista_datos(lista)


#Salida
print("\nEso era...")