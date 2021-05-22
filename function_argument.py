
# value type n değişkeninin içine name değişkeninin içindeki değer kopyalanır 
def change_name(n):
    n='ada'

name='yiğit'
change_name(name)
print(name)

# referans type 
def change(n):
    n[0]='istanbul'

sehirler=['ankara','izmir'] 
change(sehirler) # n parametresine sehirler dizisinin adresi gönderiliyor.o da artık aynı adresi taşıdığından sehirler dizisinin ilk indexini değiştirmiştir.
print(sehirler) 

def add (a,b,c=0): # iki parametre versek de 3 parametre versek de çalışır ,2 parametre verirsek c=0 olarak algılanır
    return sum( (a,b,c) )
print(add(10,20,30))
print(add(10,20))

def add2(*params): # esnek parametre verebilme imkanı kafana göre takıl * tek yıldız bir tuple listesi oluşturacağının habercisidir
    print(params)  # (10, 202, 30) basar
    print(params[1])
    return sum((params))

print(add2(10,202,30))
print(add2(10,20,24,24,2))

def display_user(**params):
    print(params)
    for key,value in params.items():
        print(f'{key} is {value}')
    print('#'*20)    

display_user(name='yusuf',age=21,city='bursa')
display_user(name='kadir',age=25,city='istanbul')
display_user(name='ahmet',age=26,city='USA')

def my_func(a,b,c,*params1,**params2):
    print(a)
    print(b)
    print(c)
    print(params1) # (23, 54, 12) tuple list basar 
    print(params2) # {'name': 'yusuf', 'age': 21} dic list basar
my_func(5,'istanbul',3.24,23,54,12,name='yusuf',age=21)

#################################################################
def convert_list(*params):
    liste=[]
    for param in params:
        liste.append(param)
    return liste
print(convert_list(1,2,4,5,6,7,8,'istanbul'))
#     #    #     #     #  gönderilen 2 asal sayı arasındaki tüm asal sayıları bulan program       #     #    #    #     # 
def asal_mi(sayi):
    i=2
    asal_mi=True
    while i < sayi:
        if(sayi%i==0):
            asal_mi=False
            break
        i+=1
    return asal_mi

sayi1 = int(input('başlangıç sayısını girin: '))
sayi2 = int(input('bitiş sayısını girin: '))
while sayi1<=sayi2:
    if(asal_mi(sayi1)):
        print(f'{sayi1} asal bir sayıdır.')

    sayi1+=1
def tam_bolenler_bul(sayi):
    tam_bolenler=[]
    for i in range(2,sayi):
        if(sayi%i==0):
            tam_bolenler.append(i)
    return tam_bolenler

print(tam_bolenler_bul(100))
