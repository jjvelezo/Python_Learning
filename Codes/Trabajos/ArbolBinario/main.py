from arbolBinario import Arbol

arbol_numeros = Arbol(5)
arbol_numeros.agregar(1984)
arbol_numeros.agregar(60)
arbol_numeros.agregar(10)
arbol_numeros.agregar(20)
arbol_numeros.agregar(1)
arbol_numeros.agregar(2013)
numeroNuevo = int(input("Ingresa algo para agregar al árbol: "))
arbol_numeros.agregar(numeroNuevo)

arbol_numeros.inorden()
