# Juan Jose Velez Orozco - 202110009010

from nodo import Nodo
from ArbolBinario import Arbol


a = input("Operador Aritmetico(+, -, /, *): ")
root = Nodo(a)
  
b = input("Primer Operando(#): ")
root.left = Nodo(b)
print("  " + a)
print(" / ")
print(b)

c = input("Segundo Operando(#): ")
root.right = Nodo(c)
print("   " +a+ "   ")
print(" /   \ ")
print(b + "     "+ c)



arbolpepito = Arbol()

print("Resultado:")
print(arbolpepito.evaluar_arbol(root))
