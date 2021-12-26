simbolo = input("Escribe el simbolo de la ecuacion que desea realizar (+, -, / ,x) ")


while simbolo == "+":

 if simbolo == "+":

  print("------------------")
  print("Numero a sumar: ")
  num1 = input()
  print("+")
  num2 = input()
  num3 = int(num1)
  num4 = int(num2)
  res = num3 + num4
  print("= ", res)
  print("------------------")

  simbolo = input("Escribe el simbolo de la ecuacion que desea realizar (+, -, / ,x) ")

  
while simbolo == "-":

 if simbolo == "-":

  print("------------------")
  print("Numero a restar: ")
  num1 = input()
  print("-")
  num2 = input()
  num3 = int(num1)
  num4 = int(num2)
  res = num3 - num4
  print("=", res)
  print("------------------")

 simbolo = input("Escribe el simbolo de la ecuacion que desea realizar (+, -, / ,x) ")

while simbolo == "/":

 if simbolo == "/":

  print("------------------")
  print("Numero a Dividir: ")
  num1 = input()
  print("÷")
  num2 = input()
  num3 = int(num1)
  num4 = int(num2)
  res = num3 / num4
  print("=", res)
  print("------------------")

 simbolo = input("Escribe el simbolo de la ecuacion que desea realizar (+, -, / ,x) ")

while simbolo == "x":

 if simbolo == "x":

  print("------------------")
  print("Numero a Multiplicar: ")
  num1 = input()
  print("x")
  num2 = input()
  num3 = int(num1)
  num4 = int(num2)
  res = num3 * num4
  print("=", res)
  print("------------------")

 simbolo = input("Escribe el simbolo de la ecuacion que desea realizar (+, -, / ,x) ")
