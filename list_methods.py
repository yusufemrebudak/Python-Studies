numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']
val = min(numbers)
print(val)  # 1 yazar
val = max(numbers)
print(val)  # 16 yazar
val = min(letters)
print(val) # a yazar
val = max(letters)
print(val) # y yazar
val=numbers[:3] # 3.indexe kadar yaz
print(val) 
#     #     #     #     #       #      #    #
numbers.append(49)  # en sona ekler
numbers.insert(3,23) # 3.indexin olduğu yere 23 rakamını  çak geri kalanları bir sağa kaydırarak listeyi tamamlaekle
numbers.insert(-1,52) # en sona çaktı orjinaldeki son eleman bir sağa kaydı [1, 10, 5, 23, 16, 4, 9, 10, 52, 49] 49 son elemandı hala son eleman
print(numbers)
#     #     #     #     #       #      #    #
numbers.pop() # en  sondaki elemanı siler  numbers.pop()=numbers.pop(-1)
numbers.pop(0) #0.indeksi siler yani ilk elemanı uçurur
print(numbers)
#     #     #     #     #       #      #    #
numbers.remove(5)  # remove methodu verilen parametredeki elemanı siler 5 elemanı silindi
print(numbers)

numbers.sort()  # küçükten büyüğe sıralar letters.sort()-->alfabetik olarak sıralar
print(numbers)
numbers.reverse() # diziyi ters çevirdi 
print(numbers)
print(numbers.count(10))  # kaç tane 10 var numberrs listesinde
numbers.clear()
print(numbers)