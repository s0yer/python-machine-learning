from sklearn import linear_model
import pandas
import datetime
#min = 55
#max = 555
#size = random.randrange(5,55)

#lista_random_x = numpy.random.uniform(min, max, size)
#lista_random_x2 = numpy.random.uniform(min, max, size)
#lista_random_y = numpy.random.uniform(min, max, size)

df = pandas.read_csv("data-func-cust-rend.csv")

X = df[['RendLiq', 'Custos']]
y = df['QtdFuncionarios']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedFunc = regr.predict([[30000, 40000]])
agora = datetime.date.today()

print("previsao - valor: ")
print(predictedFunc)

#salva dados em txt
stringSave = agora + ": Previsao -> " + predictedFunc
file = open("log_execucoes_mach_learning.txt", "a")

file.write(stringSave)
file.write(agora)
file.write(predictedFunc)

file.close()