x = int(input("x?: "))
fact = 1

while x > 1:
  
  fact = fact*x
  x = x-1

  

if x == 0:
  fact = 1

print(fact)
