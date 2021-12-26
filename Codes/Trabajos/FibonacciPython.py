def fibona(x):
  a = 0
  b = 1



  for y in range(n):
    c = a+b
    a = b
    b = c

  return b

for n in range(10):
  print(fibona(n))
