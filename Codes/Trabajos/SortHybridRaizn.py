import time
import math

inicio = time.perf_counter()



def insertion_sort(per, menor, n):

	for i in range(menor + 1, n + 1):
		valor = per[i]
		j = i

		while j>menor and per[j-1]>valor:

			per[j]= per[j-1]
			j-= 1
		per[j]= valor


def particion(per, menor, mayor):

	pos = per[mayor]
	i = j = menor

	for i in range(menor, mayor):
		if per[i]<pos:
			a[i], a[j]= a[j], a[i]
			j+= 1
	a[j], a[mayor]= a[mayor], a[j]
	return j


def quick_sort(per, menor, mayor):

	if menor<mayor:
		pos = particion(per, menor, mayor)
		quick_sort(per, menor, pos-1)
		quick_sort(per, pos + 1, mayor)
		return per


def hybrid_quick_sort(per, menor, mayor):

	while menor<mayor:


		if mayor-menor + 1<10:
			insertion_sort(per, menor, mayor)
			break

		else:
			pos = particion(per, menor, mayor)

			if pos-menor<mayor-pos:
				hybrid_quick_sort(per, menor, pos-1)
				menor = pos + 1
			else:
				
				hybrid_quick_sort(per, pos + 1, mayor)
				mayor = pos-1


a = [1, 4, 9, 40, 2, 69, 73, 15, 53, 44]


for x in a:
  hybrid_quick_sort(a, 0, 9)

  z = math.sqrt(x)
  
  
  
  print(z)
  


final = time.perf_counter()


print("Tiempo: ")
print(final - inicio)
