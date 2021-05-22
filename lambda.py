def square(n): return n**2
numbers=[1,2,3,4,5]
# map() methodu verilen dizideki elemanları verilen fonksşyona tek tek gönderir ve sonuçlarınıda tek tek döner
print(map(square,numbers))   #  <map object at 0x00B2B2C8> yazar bunu liste çevirmeliyiz
print(list(map(square,numbers))) # [1, 4, 9, 16, 25] basar

numbers=[1,2,3,4,5,6,6,7,8]
print(list(map(lambda num: num**2 ,numbers))) # isimsiz anlamına gelen bir lambda methodu yazıyorum bir daha ekstra isim verip iş yükünü arttırmamak için
square = lambda num : num**3
print(list(map(square,numbers)))  # [8, 64, 216, 512] basar 
result= list(filter(lambda num: num%2==0,numbers))
print(result) # [2, 4, 6, 6, 8] basar

################################# GLOBAL - LOCAL VARİABLES ###########################
# global scope

x='global x'


def func():
    #local scope
    x='local x'

func()
print(x)
#####################
name='çınar'
def change_name(new_name):
    name=new_name  # local bölgede olduğumuzdan name yeni bir tanımlamadır ve dışardaki name den bağımısızdır 
    print(name)  #ada yazar  

change_name('ada')
print(name) # çınar yazar  buradaki 'name' global olarak tanımlanan name 'i alır
########################################################
print('*'*50)
name='global string'
def greeting():
    #name = 'Çınar'
    print(name)  # global string yazar
    def hello():
        name = 'ada'
        print(name) # ada yazar
    
   
    
    hello()
print(name) # global string yazar
greeting()
########## local de kullanılan değişkenler aynı isimde olan dışarıdaki değişkenler etkilemez bunun için 'global' keywordu kullanılmalı

x=40
def test(): # bunu yazdıktan sonra artık local bölgede kullanacağımız x global bölgede tanımlanan x dir 
    global x 
    print(f'x :{x}')
    x=100 # global x 100 oldu
    print(f'changed x to {x}')
test()
print(x)