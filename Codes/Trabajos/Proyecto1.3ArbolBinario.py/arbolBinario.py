class Arbol:
    def __init__(self):
        pass

    def evaluar_arbol(self, raiz):
        if raiz is None:
            return 0
        if raiz.left is None and raiz.right is None:
            return int(raiz.dato)
        left_sum = self.evaluar_arbol(raiz.left)
        right_sum = self.evaluar_arbol(raiz.right)
        if raiz.dato == '+':
            return left_sum + right_sum
        elif raiz.dato == '-':
            return left_sum - right_sum
        elif raiz.dato == '*':
            return left_sum * right_sum
        else:
            return left_sum / right_sum
