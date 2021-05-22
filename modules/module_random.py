import random

# result=dir(random)
# result=help(random)
# print(result) 
# random modulunun fonksiyonları dökümana olarak gelir.
result = random.random() # 0.0-1.0 arası sayı üretilir
print(result)

result = int(random.uniform(1,100)) #ondalıklı sayı üretilir eğer int() içine alırsak tam sayı üretir 
print(result)
result = random.randint(1,100) # direkt olarak int sayı üretir
print(result)
#   #   #   #   #   #   #   #   #   #   #   #   #
names = ['ali','yağmur','deniz','cenk','ahmet','yusuf']
result = names[random.randint(0,len(names)-1)]
result=random.choice(names) # diziden rastgele eleman seçer
print(result)
liste = list(range(10))
print(liste) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] yazar
random.shuffle(liste) # liste elemanları karılır.
print(liste)

liste = range(100)
result = random.sample(liste,4)
print(result)