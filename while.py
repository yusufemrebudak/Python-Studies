# x=0
# while x<100:
#     print(x)
#     x+=1


# numbers=[]
# i=0
# while i<5 :
#     sayi=int(input('sayı : '))
#     numbers.append(sayi)
#     i+=1
# numbers.sort()
# print(numbers)
 ################# NICE APP ##################################33

# urunler=[]
# adet = int(input('kaç adet ürün eklemek istiyorsunuz : '))
# i=0
# while( i<adet ):
#     name = input('ürün ismi: ')
#     price = int(input('ürün fiyatı: '))
#     urunler.append({
#         'name':name,
#         'price':price
#     })
#     i+=1
# for urun in urunler:
#     print(f'urun adı: {urun["name"]} , urun fiyat: {urun["price"]}')

##############   BREAK-CONTUNİUE  ###############
name = 'yusuf budak'
for letter in name :
    if (letter==' '):
        break # döngüyü bitirir
    print(letter)

for letter in name :
    if (letter=='f'):
        continue # döngüyü devam ettirir
    print(letter)
