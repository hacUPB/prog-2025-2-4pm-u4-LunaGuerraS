#Crear una lista vacia.
Lista = ()

#Añadir un elemento a la lista.
Lista.append(56)
print(Lista)

#Añadir un elemento que ingrese el usuario
numero = int(input("Ingrese un numero por favor: "))
Lista.append(numero)

#Ingresar un numero aleatorio 10 veces.
import random

for i in range (10):
    aleat = random.randit(0,100)
    Lista.append(aleat)
print (Lista)