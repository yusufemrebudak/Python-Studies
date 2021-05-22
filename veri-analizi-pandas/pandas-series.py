import pandas as pd
import numpy as np

numbers = [20,30,40,50,60]
letters = ['a','b','c','d',20]
scalar = 5

pandas_series = pd.Series(letters) # bir pandas serisi oluşturduk
# string bir bilgi veya string int karışık bir bilgi Series içine tanımlanırsa bize object döner
print(pandas_series) # 0     a
# 1     b
# 2     c
# 3     d
# 4    20

pandas_series = pd.Series(numbers) # bir pandas serisi oluşturduk
# int bilgi tanımlarsak parametre olarak bize type olarak int64 döner

print(pandas_series) # 0    20
# 1    30
# 2    40
# 3    50
# 4    60
numbers1 = [1,2,3,4,5]
pandas_series = pd.Series(numbers1,['a','b','c','d','e']) #a    1
# b    2
# c    3
# d    4
# e    5

dic={'a':10,'b':20,'c':30,'d':40}
pandas_series = pd.Series(dic)
print(pandas_series) #a    10
# b    20
# c    30
# d    40

random_numbers = np.random.randint(0,100,6)
pandas_series = pd.Series(random_numbers) #a    1
print(pandas_series)# 0    57
# 1    44
# 2    37
# 3    85
# 4    20
# 5    40

pandas_series = pd.Series(numbers1,['a','b','c','d','e']) 
# a    1
# b    2
# c    3
# d    4
# e    5
result = pandas_series[0]
print(result) # 1 verir
result = pandas_series[:2]
print(result) # a    1
# b    2
result = pandas_series[2:]
print(result) # c    3
# d    4
# e    5
result = pandas_series['c']
print(result) # 3 yazar

##############################################

opel2018 = pd.Series([20,30,40,10],['astra','corsa','mokka','insignia'])
opel2019 = pd.Series([40,30,20,10],['astra','corsa','Grandland','insignia'])

total = opel2018 + opel2019 # mokka bilgisine karşılık diğer listede mokka bilgisine karşılık bir değer olmadığı için mokka karşısında NaN Yazar
# aynı şey Grandland içinde geçerli
print(total) #Grandland     NaN
# astra        60.0
# corsa        60.0
# insignia     20.0
# mokka         NaN
print(total['astra']) # 60.0 yazar.