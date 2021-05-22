# x = 10

# if x>5:
#     raise Exception('x 5 den büyük değer alamaz.') # en basit haliyle

def chech_password(psw):
    import re # regular experssion modulunu import edicem..
    if len(psw)<8:
        raise Exception('Parola en az 7 karakter olmalıdır.')   

    elif not re.search("[a-z]",psw): 
        raise Exception('Parola küçük harf içermelidir.')

    elif not re.search("[A-Z]",psw): 
        raise Exception('Parola büyük harf içermelidir.')

    elif not re.search("[0-9]",psw): 
        raise Exception('Parola rakam içermelidir.')
    elif not re.search("[_@$]",psw): 
        raise Exception('Parola alpha numeric karakter içermelidir.')
    elif re.search("[\s]",psw): 
        raise Exception('Parola boşluk içermemelidir.')
    else:
        print('geçerli parola')


password='12345678aA/@'

try:
    chech_password(password) # burdan çıkacak olan hatayı catch de yakalıyoruz.

except Exception as ex:
    print(ex)
else:
    print("geçerli parola")
finally:
    print("validation tamamlandı")
#######################################################################################3
class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception('name alanı fazla karakter içeriyor.')
        else:
            self.name = name 
        
p1=Person('Ali',1998)
print(p1.name)
############################################## UYGULAMA ##############################################
print('#'*80)
liste=['1','2','5a','10b','abc','19','50']
new_list=[]
for item in liste:
    try:
        new_list.append(int(item))
    except Exception as ex:
        print(ex)
    else:
        print(f'{item} listeye eklendi')
print(new_list)
############################################## UYGULAMA ##############################################
print('#'*80)

while True:
    sayi=input('Bir sayi girin:')
    if sayi=='q':
        break
    try:
        result=int(sayi)  
        print(f'Girdiğiniz sayi : {result}')  
        break
    except Exception:
        print('Geçersiz sayı')
        continue
############################################## UYGULAMA ##############################################
print('#'*80)
def checkPassword(parola):
    turkce_karakterler='şçğüöıİ'
    for i in parola:
        if i in turkce_karakterler:
            raise TypeError('Parola türkçe karakter içermemelidir.')
        else: 
            pass
    print("geçerli parola")
parola = input('Parola: ')
try:
    checkPassword(parola)
except TypeError as err:
    print(err)

############################################## UYGULAMA ##############################################
print('#'*80)
def faktoriyel(x):
    x = int(x)
    if x<0:
        raise ValueError('negatif değer')
    result = 1
    for i in range(1,x+1): # x+1 yapmamızın nedeni x değerini de almamız.
        result*=i
    return result

for x in [4,-2,5,6,-7,'10a']:
    try:
        y = faktoriyel(x)
        print(y)
    except ValueError as err:
        print(err)
        continue
