fruits={'orange','apple','banana'}
print(fruits)
# print(fruits[0]) indekslemez bir liste türüdür ondan dolayı sıralamazdır sort ile filan
fruits.add('cherry') 
fruits.update(['grape','mango','orange']) # orange sets de olduğu için orange eklenmedi
print(fruits)
print(type(fruits))

my_list = [1,2,5,4,4,2,1] # set()methodu set veri yapısına çevirir verilen listeyi
my_newlist=set(my_list) 
print(my_newlist)
fruits.remove('mango') # 12-13. satırlar elemanları siler 
fruits.discard('apple')
print(fruits)
fruits.clear()
print(fruits)
