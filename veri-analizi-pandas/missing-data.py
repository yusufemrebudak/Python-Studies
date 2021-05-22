import pandas as pd 
import numpy as np 
data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index = ['a','c','e','f','h'] ,columns = ['column1',"column2","column3"])
df = df.reindex(['a','b','c','d','e','f','g','h'])
result = df
print(result)
result = df.drop("column1",axis = 1) #axis =1 kolon silme , axis=0 satır silme
print(result)
result = df.drop(["column1","column2"],axis = 1) #axis =1 kolon silme , axis=0 satır silme
print(result)
result = df.drop(["a","b","c"],axis = 0) #axis =1 kolon silme , axis=0 satır silme , a-b-c satırlarını silme
print(result)
result = df.notnull()
print(result)
#  column1  column2  column3
# a     True     True     True
# b    False    False    False
# c     True     True     True
# d    False    False    False
# e     True     True     True
# f     True     True     True
# g    False    False    False
# h     True     True     True
result = df["column1"].isnull().sum()
print(result) # 3 yazar
print(df)
new_column = [ np.nan , 10 , np.nan , 12 , np.nan , 42 , np.nan , 73 ]
df["column4"] = new_column
print(df)
result = df[df["column1"].isnull()] # kolon1 deki null değerleri olan kayıtları getir.
print(result)
result = df[df["column1"].isnull()]["column1"] # kolon1 deki null değerleri olan kayıtların kolon1 kdeğerlerini getir sadece 
print(result)
result = df.dropna() #drop dan farkı nan değerleri olan satır veya sutunlarıı siler default olarak axia=0 satırları getirmez yani nan değeri olan
print(result) #sadece f ve h satırları geldi yani sadece f ve h satırlarında nan değer yok demektir
#  column1  column2  column3  column4
# f     90.0     86.0     43.0     42.0
# h     74.0     52.0     63.0     73.0
result = df.dropna(axis=1) 
print(result) #boş değer gelir çünkü her kolonda en az 1 tane nan vardır
result = df.dropna(how="any") 
print(result)
result = df.dropna(how="all")  # yalnızca g saatırındaki tüm değerler nan idi geri kalan tüm satırlar getirildi
print(result)
result = df.dropna(subset = ["column1","column2"] , how="all") # nan değerini önemsediğimiz sutunları belirtiriz diğerleriyle ilgilenmeyiz ve all dersek iki kolondada nan olması lazım değerlerin
# iki kolondada nan değeri olan kayıtları getirmiyor
print(result) # b ve d ve g satırlarında kolon1 ve kolon2 nan idi ondan dolayı a-c-e-f-h satırları geldi 
result = df.dropna(subset = ["column1","column2"] , how="any") # nan değerini önemsediğimiz sutunları belirtiriz diğerleriyle ilgilenmeyiz ve all dersek iki kolondada nan olması lazım değerlerin
# iki kolondada nan değeri olan kayıtları getirmiyor
print(result)
result = df.dropna(thresh = 3) # en az 3 kolonunda veri olan satırları getir dedik 
print(result)
result = df.fillna(value = "no input") # nan alanlara no input girer 
print(result)
result = df.fillna(value = 1) # nan alanlara 1  girer 
print(result)
 
# toplam = df.sum().sum() data framdeki verilen toplam değerini verir
#gelen veride null alan varmı kontrol ederiz
result = df.isnull().sum()
print(result)
# column1    3
# column2    3
# column3    3
# column4    4
result = df.isnull().sum().sum()
print(result) # toplam 13 tane nan değer var
result = df.size # toplam veri sayısını verir
print(result)
result = df.sum()["column1"]
print(result) #kolon1 deki değerlerin toplamı
def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size-df.isnull().sum().sum()
    return toplam / adet

result = df.fillna(value = ortalama(df))
print(result)