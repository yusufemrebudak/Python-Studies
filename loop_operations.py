# range method
for item in range(2,10): # 2 den 10 a kadar olan sayıları yazdır
    print(item)

print(list(range(5,100,20)))  # [5, 25, 45, 65, 85] basar
####################  enumarete  ####################
greeting = 'hello'
for index,letter in enumerate(greeting):
    print(f'index: {index} , letter: {letter}')

for item in enumerate(greeting):
    print(item) 
#     #(0, 'h') 
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o') yazar for index,item  in enumerate(greeting) yazarsak ayrı ayrı index i ve değeri değişkenlere atarız.

################################ zip ###################################3
list1=[1,2,3,4,5]
list2=['a','b','c','d','e'] 
list3 =[100,200,300,400,500]
print(list(zip(list1,list2))) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')] olarak iki listenin de aynı indekslerini eşler (1, 'a') bunlar bir tuple list tir
print(list(zip(list1,list2,list3))) # [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]

for item in zip(list1,list2,list3):
    print(item)
for a,b,c in zip(list1,list2,list3): #her tuple daki ilk elemanı basar yani sonuc 1,2,3,4,5 alt alta basar
    print(a)
    
##########################3 LİST COMPREHENSİONS ####################### while ve for a alternatif
numbers=[]
for x in range(10):
    numbers.append(x)
print(numbers)
numbers=[x for x in range(10)]  # şu olay for veya while yerine kullanılabilir
print(numbers) # iki yöntemde de 0-10 a kadar olan sayıları bir list olarak tanımlıyoruz.
numbers=[x**2 for x in range(10)]
print(numbers) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] basar
mystring='hello'
my_list=[letter for letter in mystring]
print(my_list)  # ['h', 'e', 'l', 'l', 'o'] basar
years=[1934,1945,1995,1994]
ages=[2019-year for year in years] 
print(ages)  # [85, 74, 24, 25] basar

result = [x if x%2==0 else 'tek' for x in range(1,10)] # x in listeye dahil olması için  x%2==0 ifadesinin true dönmesini şart koşuyorum.
print(result)