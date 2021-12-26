from nodo import Nodo
from ArbolBinario import Arbol


root = Nodo('+')
root.left = Nodo('-')
root.left.left = Nodo('4')
root.left.right = Nodo('1')
root.right = Nodo('*')
root.right.left = Nodo('6')
root.right.right = Nodo('/')
root.right.right.left = Nodo('6')
root.right.right.right = Nodo('3')
arbolPepe = Arbol()

print(arbolPepe.evaluar_arbol(root))
