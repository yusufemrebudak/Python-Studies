import pandas as pd
import numpy as np 
personeller ={
    'Calisan':['Ahmet Yılmaz','Yusuf Budak','Abdulkadir Budak','Ahmet Faruk Budak','Salih efe Budak','İbrahim Budak'],
    'Departman':['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe'],
    'Yas':[40,21,24,25,11,55],
    'Semt':['Abd','Bursa','Bursa','Abd','Abd','Bursa'],
    'Maas':[5000,3000,5000,4000,4500,7000]
}
print(type(personeller))
print(personeller)
df = pd.DataFrame(personeller)
print(df)
result = df['Maas'].sum() # personellerin maaşlarının toplamı
print(result)
result = df.groupby("Departman").groups
print(result)
result = df.groupby(["Departman","Semt"]).groups
print(result)
#semtler = df.groupby("Semt")
for name,group in df.groupby("Semt"):
    print(name)
    print(group)


for name,group in df.groupby("Departman"):
    print(name)
    print(group)
print("*"*100)
for name,group in df.groupby(["Departman","Semt"]):
    print(name)
    print(group)
result = df.groupby("Semt").get_group("Bursa")
print(result)
result = df.groupby("Departman").get_group("Bilgi İşlem")
print(result)
result = df.groupby("Departman").mean() # mean() ortalama alır
print(result)
#                   Yas    Maas
# Departman
# Bilgi İşlem       16.0  3750.0
# Muhasebe          39.5  6000.0
# İnsan Kaynakları  32.5  4500.0

result = df.groupby("Departman")["Maas"].mean() # mean() ortalama alır , aynı departmandaki kişilerin maaş ortalaması alınır
print(result)
# Departman
# Bilgi İşlem         3750
# Muhasebe            6000
# İnsan Kaynakları    4500

result = df.groupby("Departman")["Calisan"].count() # count() sayar
print(result)
# Departman
# Bilgi İşlem         2
# Muhasebe            2
# İnsan Kaynakları    2

result = df.groupby("Departman")["Yas"].max() # aynı departmanda çalışan insanlardan yaşı en büyük olanları al
print(result)
# Departman
# Bilgi İşlem         21
# Muhasebe            55
# İnsan Kaynakları    40

result = df.groupby("Departman")["Maas"].max() # aynı departmanda çalışan insanlardan maaşı en büyük olanları al
print(result)
# Departman
# Bilgi İşlem         4500
# Muhasebe            7000
# İnsan Kaynakları    5000

result = df.groupby("Departman")["Maas"].max()['Muhasebe'] # muhasebe departmanda çalışan insanlardan maaşı en büyük olanı al
print(result) # 7000 yazar

result = df.groupby("Departman")["Maas"].max()['İnsan Kaynakları'] # aynı departmanda çalışan insanlardan maaşı en büyük olanları al
print(result) # 5000 yazar
result = df.groupby("Departman")["Maas"].max() # aynı departmanda çalışan insanlardan maaşı en büyük olanları al
print(result) # 5000 yazar

result = df.groupby("Departman")['Maas'].agg([np.sum,np.mean,np.max,np.min])
print(result)
#                     sum  mean  amax  amin
# Departman
# Bilgi İşlem        7500  3750  4500  3000
# Muhasebe          12000  6000  7000  5000
# İnsan Kaynakları   9000  4500  5000  4000

result = df.groupby("Departman")['Maas'].agg([np.sum,np.mean,np.max,np.min]).loc['Muhasebe']
print(result)
# sum     12000
# mean     6000
# amax     7000
# amin     5000