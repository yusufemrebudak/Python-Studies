import numpy as np


numbers = np.array([0,5,10,15,20,25,50,75,100])
result = numbers[5]
print(result) # 25 gelir , normal listelerdeki gibi bu kısmı 
result = numbers[-1]
print(result) # en sağdan başlar karşımıza 100 gelir 
result = numbers[0:3] # 0.indeksten başla 3.indekse kadar al 
print(result) # [ 0  5 10] 
result = numbers[:3] # 0.indeksten başla 3.indekse kadar al 
print(result) # [ 0  5 10] 
result = numbers[3:] # 3.indeksten başla sona kadar al 
print(result) # [ 15  20  25  50  75 100]
result = numbers[::] # tüm listeyi al  
print(result) # [  0   5  10  15  20  25  50  75 100]
result = numbers[::-1] # tüm listeyi al  tersten 1 er 1 er giderek yaz
print(result) # [100  75  50  25  20  15  10   5   0]
numbers2 = np.array([[0,5,10],[15,20,25],[50,75,100]])
print(numbers2) #[[  0   5  10]
#  [ 15  20  25]
#  [ 50  75 100]]
result = numbers2[0]
print(result) # [ 0  5 10]
result = numbers2[0,2]
print(result) # 10 yazar
result = numbers2[2,0]
print(result) # 50 yazar
result = numbers2[:,2] #tüm dizi gruplarını seçtim 2.elemanlarının hepsini aldım 
print(result)  # [ 10  25 100]
result = numbers2[:,0] #tüm dizi gruplarını seçtim 0.elemanlarının hepsini aldım 
print(result)  # [ 0 15 50]
result = numbers2[:,0:2] #tüm dizi gruplarını seçtim 0 ve 2.indeks arası elemanların hepsini aldım 
print(result) #[[ 0  5]
#[15 20]
#[50 75]]

arr1=np.arange(0,10)
arr2 = arr1 # referans adresini  kopyaladık
print(arr2) # [0 1 2 3 4 5 6 7 8 9]
print(arr1) # [0 1 2 3 4 5 6 7 8 9] 
arr2[0] = 20 # şimdi ben sadece arr2 üzer,nde değişiklik yaptım fakat arr1 de arr2 de aynı adresi gösterdikleri için arr1 de değişti.
print(arr2) # [20  1  2  3  4  5  6  7  8  9]
print(arr1) # [20  1  2  3  4  5  6  7  8  9]


arr1=np.arange(0,10)
arr3 = arr1.copy() # arr1 in içindekileri kopyalayıp farklı bir yeri gösteren arr3 e attık arr3 ve arr1 farklı yerleri gösterirler.
arr1[0] = 20 
print(arr1) # [20  1  2  3  4  5  6  7  8  9]
print(arr3) # [0  1  2  3  4  5  6  7  8  9] 
 