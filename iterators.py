liste =[1,2,3,4,5]

iterator=iter(liste) # iter metoduyla bir iterable obje gönderiyotuz ve bundan bi iterator oluşturur.bunu for dongüsü kendi yapar
print(iterator) # <list_iterator object at 0x0229B190>  list iterator objesi oluşturuldu

print(next(iterator)) # listenin 1. elemanı gelir
print(next(iterator)) # listenin 2. elemanı gelir
print(next(iterator)) # listenin 3. elemanı gelir
print(next(iterator)) # listenin 4. elemanı gelir
print(next(iterator)) # listenin 5. elemanı gelir
#print(next(iterator)) # stok ıteration hatası verir çünkü 6. eleman yoktur.

iterator=iter(liste)

while True:
    try:
        element=next(iterator)
        print(element)
    except StopIteration:
        break


class MyNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x=self.start
            self.start +=1
            return x
        else :
            raise StopIteration



list = MyNumbers(10,20)

for x in list:
    print(x) # önce list den iterator ü çeker sonra her döngüde next i çalıştırır.

