#import pandas
from sklearn import linear_model
import numpy


#df = pandas.read_csv("cars.csv")


min = 55
max = 555
size = random.randrange(5,55)

lista_random_x = numpy.random.uniform(min, max, size)
lista_random_x2 = numpy.random.uniform(min, max, size)
lista_random_y = numpy.random.uniform(min, max, size)


predicted = regr.predict([[2300, 1300]])

#salva dados em txt
file = open("log_execucoes_mach_learning.txt", "a")
file.write(data)
file.close()


X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
print("previsao - valor: ")
print(predicted)

