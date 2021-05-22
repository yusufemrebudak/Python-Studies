names=['Ali','Yağmur','Hakan','Deniz']
years=[1998,2000,1998,1987]
names.append('Cenk')  #listenin sonuna 'cenk' ekleyin 
names.insert(0,'Sena') #listenin başına 'sena' ekleyin 
names.remove('Deniz') # listeden deniz ismini silin
index=names.index('Yağmur')
print(index)
names.pop(index) #index=3 ise 3. indexteki değeri siler
result='Ali' in names  # names listesinde 'ali' varmı
print(result)
result=names.index('Cenk') # 'cenk' listede hangi indexte ise onu döner
print(result)
str='Chevrolet,Dacia,Toyota' # stringi diziye çevirin
result=str.split(',')
print(result[1]) # 'dacia' basar
min=min(years)
max=max(years)
print(f'min :{min} max:{max}')
############ kullanıcıdan alacağınız 3 tane markayı liste olarak saklayın ##################

markalar=[]

marka=input("Marka:")
markalar.append(marka)

marka=input("Marka:")
markalar.append(marka)

marka=input("Marka:")
markalar.append(marka)
print(markalar)



