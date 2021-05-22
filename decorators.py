# decorator fonksiyonlar bir fonksiyona özellik eklemek istediğimizde kullanıyoruz
# bir çok fonksiyonla ilişkilendirilebilir.
def my_decorator(func):
    def wrapper(name):
        print('wrapper ',wrapper)
        print('fonksiyondan önce işlemler')
        func(name)
        print(func)
        print('fonksiyondan sonraki işlemler')
    return wrapper

@my_decorator   # bunu yazdıktan sonra decorator fonksiyonuna say_hello fonksiyonunu gönderilir.
def say_hello(name): 
    print('hello '+name)
    

def say_greeting():
    print('greeting')

print(say_hello)


say_hello('ali')
# say hello == wrapper oldu aynı adresi taşırlar fakat func artık say hello nun adresini taşır

# say_hello = my_decorator(say_hello) # func=say_hello set ettik daha sonra fonkdan dönen wrapperın adreside say_hello ya set edildi.
# say_hello()
# say_greeting = my_decorator(say_greeting)
# say_greeting()

#############################################################################33
import math
import time

def calculate_time(func): #decorator fonksiyon
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print('Fonksiyon '+func.__name__ +' '+str(finish-start) +' saniye sürdü')
    return inner

@calculate_time
def usalma(a,b): 
    print(math.pow(a,b))


@calculate_time
def factorial(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b,c,d):
    print(a+b+c+d)


usalma(3,4)
factorial(5)
toplama(10,20,30,40)












