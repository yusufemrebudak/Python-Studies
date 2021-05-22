import pandas as pd 
data = pd.read_csv("imdb_top_list.csv")
print(data)
data.dropna(inplace = True)
data["Title"] = data["Title"].str.upper()
print(data)
data["Title"] = data["Title"].str.lower()
print(data)
data["column-x"] = data["Title"].str.find("the") # ilgili satırın Title ına bakar title da the kelimesi geçtiyse kaçıncı harfinde döndüğünü 
#ilgili satırın column-x sutununa set eder
print(data)
result = data["Title"].str.contains('the').head(30) # ilk 30 kayıta bakar ve title alanında the olan kayıtları verir
print(result)
result = data[data.Title.str.contains('the')].head(20) # ilk 30 kayıta bakar ve title alanında the olan kayıtları verir
print(result)
# data = data.Title.str.replace(' ','-') # title içindeki tüm boşluk karakterlerinin arsına - koyar
# print(data.head(10))
result = data[2:20]["Title"]
print(result)