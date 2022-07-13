# mean, median, mode

import random
import numpy
from scipy import stats

lista_random = []

size = random.randrange(5,55)

i=0
while i < size:
    lista_random.append(random.randrange(5,555))
    i += 1

print(len(lista_random))
print(lista_random)

x_media = numpy.mean(lista_random)
x_mediana = numpy.median(lista_random)
x_moda = stats.mode(lista_random)

print(x_media)
print(x_mediana)
print(x_moda)
