import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
print(data)
# [[10 95 49 47 48]
#  [94 10 30 57 31]
#  [65 55 72 23 14]
#  [91 66 81 29 70]
#  [13 50 27 55 10]
#  [88 37 77 83 24]
#  [60 91 55 72 25]
#  [39 42 33 80 57]
#  [82 77 46 32 35]
#  [83 55 77 79 81]
#  [29 50 64 33 61]
#  [16 42 82 58 52]
#  [16 45 30 86 51]
#  [50 57 85 43 66]
#  [42 60 83 71 76]]
df = pd.DataFrame(data,columns = ["Column-1","Column-2","Column-3","Column-4","Column-5"])
# df.columns # kolon bilgilerini verir
#result = df.head() # ilk 5 kaydı verir
#result = df.head(10) # ilk 10 kaydı verir
#result = df.tail() # son 5  kaydı verir
#result = df.tail(10) # son 10  kaydı verir
result = df["Column-1"].head() #Columns-1 in head ini çağırıyoruz. yani ilk 5 kaydın column-1 değerini 
result = df[["Column-1","Column-2"]].head() # kolon1 ve kolon2 ilk 5 kaydı geldi
result = df[5:15][["Column-1","Column-2"]] # 3den 15i satıra kadar kolon1 ve kolon2 nin değerlerini alırız 
print(result)
############## FİLTRELEME İŞLEMLERİ #################
result = df>50 # tüm değerlere bakar 50 üstü olanları TRUE döner olmayanları FALSE döner
print(result)
result = df[df>50] # tüm değerlere bakar 50 üstü olanları döner olmayanları NaN döner
print(result)
result = df[ (df["Column-1"]>20) & (df["Column-2"]>30) ][["Column-1","Column-2"]] #kolon1 ve kolon2 değerleri 50 den büyük kayıtların kolon1-kolon2 değerleri getirilir
print(result)
# result = df.query("Column-1 >= 50")
# print(result)