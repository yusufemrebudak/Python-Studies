# names=['yusuf','ahmet','kadir']
# for name in names:
#     print('my name is '+ name)
name = 'yusuf budak'
for n in name : 
    print(n) # tek tek stringin karakterlerini basar.

tup=(1,2,3,4,5)
print(type(tup) ) #tuple sınıfından 
print(tup[1]) # ekrana 1 basar
for t in tup:
    print(t) #1,2,3,4,5 i sırayla tek tek basar.
tup=[(1,2),(1,3),(3,5),(5,7)]
print(type(tup)) # list sınıfındandır
for a,b in tup:
    print(a,b) # alt alta  sırasıyla 1,2 - 1,3 -  3,5 - 5,7 basar
    
dic={'k1':1 , 'k2':2 , 'k3':3} # key--> value karşılığı
for key,value in dic.items():
    print(key,value)  # k1 1
# k2 2
# k3 3 basar 

urunler=[ 
    {'name':'samsung s6','price':'3000'}, 
    {'name':'samsung s7','price':'4000'}, 
    {'name':'samsung s8','price':'5000'},    # bir ürünler listemiz var ve her bir liste elemanı sözlük(dictionary) veri tipinde.
    {'name':'samsung s9','price':'6000'},
    {'name':'samsung s10','price':'7000'}
]


    #print(urun)
# {'name': 'samsung s6', 'price': '3000'}
# {'name': 'samsung s7', 'price': '4000'}
# {'name': 'samsung s8', 'price': '5000'}
# {'name': 'samsung s9', 'price': '6000'} 
# {'name': 'samsung s10', 'price': '7000'}   yazar
toplam=0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam +=fiyat
print('toplam ürün fiyatı '+str(toplam)) # 25000 yazar
# 3000
# 4000
# 5000
# 6000
# 7000 yazar


