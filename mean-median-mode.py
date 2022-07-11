
import random
import numpy

lista_random = []

size = random.randrange(5,55)

i=0
while i < size:
    lista_random.append(random.randrange(5,555))
    i += 1

print(len(lista_random))
print(lista_random)

xmean = numpy.mean(lista_random)

print(xmean)
