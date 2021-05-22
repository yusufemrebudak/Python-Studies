


x=input('1.sayi:') # inputtan gelen değer default olarak string  algılanır exp=2
y=input('2.sayi:')# inputtan gelen değer default olarak string  algılanır exp =4
toplam = x+y # bu sebeple toplam =iki sayının yan yana yazılmasıdır toplam=24
print(x+y) #  print 24
print(type (x))
print(type(y))
print(int(x)+int(y)) #tip dönüşümlerini yaptığımdan dolayı 6 yazdı
####################################################################################
x =5
y =2.3
name = 'yusuf'
is_online = True
'''
print(type(x))            <class 'int'>
print(type(y))                <class 'float'>
print(type(name))               <class 'str'>
print(type(is_online))          <class 'bool'>
'''
'''
y=int(y)
print(y)  # y yukarda 2.3 idi fakat biz floattan int e çevirdiğimiz için 2 yazdı sadece
'''
is_online = int(is_online) # true 'nun int e çevrilmiş hali 1 dir false ' un ise 0 dır
print(is_online)


######################## r veriliğ daire yarıçağı ve alanı bulduran program ########################
r=input('yarıçap giriniz :')
r = float(r)
print('Çevre : ',str(2*3.14*r),' alan : ',str(3.14*(r**2)))# bulduğumuz sonuçları tekrardan stringe çevirdik
