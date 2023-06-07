print("--------------------------------")
print("- BUSCAR UN NUMERO EN CONJUNTO -")
print("--------------------------------")

#Entrada
dato = int(input("Número a buscar: ")) #se recibe el dato del usuario

#Procesamiento
a = [1,2,3,4,5] #Se almacena una lista de datos
r = False

for i in a:
    if i == a:
        print("Lo encontré...")
        r = True

if r == False:
    print("No lo encontré...")

#Salida
print("\nEso era...")