import random


nombre = input("¿Cual es tu nombre? ")
print("Buenos dias " + nombre + ", intenta adivinar un nummero entre el 1 y el 10: ")


azar = random.randint(1, 2)
print(azar)

numero = input()


if numero == azar:
  print("Correcto")
 
if numero != azar:
 print("Vuelve a intentarlo: ")
 numero = input()
 
