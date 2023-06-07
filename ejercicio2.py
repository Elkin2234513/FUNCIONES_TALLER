#Construir una función que reciba una cadena digitada (como parámetro) por el usuario y que lo muestre n veces en la pantalla. El valor de n también es digitado por el usuario.

print("--------------------------------")
print("-- MOSTRAR CADENA N VECES EN ---")
print("---------- PANTALLLA -----------")
print("--------------------------------")

#Definición de la función
def mostrarNombre(cadena, n):
    for i in range(1,n):
        print(cadena, i)
        
    pass


#Entrada

cadena = input("DIGITE LA CADENA: ")

n = int(input("DIGITE LAS VECES QUE QUIERE IMPRIMIR: "))

#Procesamiento
mostrarNombre(cadena, n+1)


#Salida
print("\nEso era...")