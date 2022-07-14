# mean, median, mode

import random
import numpy
import matplotlib.pyplot as plt

min = 55
max = 555
size = random.randrange(5,55)
lista_random = numpy.random.uniform(min, max, size)

print(size)
print(len(lista_random))
print(lista_random)
print("-----------------------------")

# desenha histograma
plt.hist(lista_random, 555)
plt.show()
