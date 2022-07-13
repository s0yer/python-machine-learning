# standard deviation

import random
import numpy

lista_random = []

size = random.randrange(5,55)

i=0
while i < size:
    lista_random.append(random.randrange(100,555))
    i += 1

print(len(lista_random))
print(lista_random)

x_desviopadrao = numpy.std(lista_random)

print(x_desviopadrao)

#percentagem
p = numpy.percentile(lista_random, 250)
print(p)