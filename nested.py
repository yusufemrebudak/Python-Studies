def greeting(name):
    print('hello '+name)

greeting('ali')

say_hello=greeting # greeting değişkeni fonksiyonun adresini tutuyordu artık say_hello da o adresi tutuyor bundan dolayı say_hello üzerinden
# de fonksiyonu çalıştırabiliriz.
print(say_hello) # <function greeting at 0x01BEB538> yani fonksiyonlarda birer obje gibi yer tutar hafızada ve greeting değişkeni 
# aslında o objenin adresini tutar
print(greeting) # <function greeting at 0x01BEB538>
say_hello('ali')
del say_hello
greeting('ali') 
###############################################################################
#encapsulation
def outer(num1):
    print(f'outer çalıştı {num1}')
    def inner_increment(num1):
        num1 +=1
        print(f'inner çalıştı {num1} ')
        return num1
    num2 = inner_increment(num1)
    print(num1,num2) 
outer(10)
# inner_increment(10) hata verir çünkü sadece outer kapsamında çalıştırılacak bir fonksiyon
def factorial(number): # önce sayıyı filtreleme işlemine tabii tutarız girilen değer gerçekten pozitif ve number ise o zaman faktoriyel alma işlemine tabii tutabiliriz.

    if not (isinstance(number,int)):
        raise TypeError('number must be an integer')
    if not number>=0:
        raise ValueError('number must be zero or positive')

    def inner_factorial(number):
        if number<=1:
            return 1
        return number * inner_factorial(number-1)
        # 5*inner(4)->5*4*inner(3)-->5*4*3*inner(2)-->5*4*3*2*inner(1)-->5*4*3*2*1
    return inner_factorial(number)
try:
    print(factorial(-1))
except Exception as ex:
    print(ex)
######################################################################################
def usalma(number):

    def inner(pow):
        return number ** pow
    return inner

two = usalma(2) # inner fonksiyonunun adresi two ya atanır ve number 2 ye set edilir
three=usalma(3) # inner fonksiyonunun adresi three ye de atanır ve number 3 ye set edilir
print(two(3)) # inneri çağırırır number zaten 2 ye set edilmişti pow da 3 e set edildi ve 2üzeri3 = 8 basar.
print(three(4)) # inneri çağırırır number zaten 3 ye set edilmişti pow da 4 e set edildi ve 3üzeri4 = 81 basar.
######################################################################################
def yetki_sorgula(page):
    
    def inner(role):
        if role=='admin':
            return f'{role} rolünün {page} sayfasına ulaşabilir.'
        else:
            return f'{role} rolünün {page} sayfasına ulaşamaz.'

    return inner

user1=yetki_sorgula('Product Edit')
print(user1('admin'))
######################################################################################
def islem(islem_adi):

    def toplam(*args):
        toplam = 0
        for i in args:
            toplam +=i
        return toplam

    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    
    if islem_adi=='toplama':
        return toplam
    else:
        return carpma
toplama=islem('toplama')
carpma=islem('carpma')
result_toplam=toplama(1,2,3,4,5,6)
result_carpma = carpma(1,2,3,4,5,6)
print(result_toplam)
print(result_carpma)