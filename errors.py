# error -> hata
# print(a) -->NameError
# int('1a2') --> ValueError
# print(10/0) --> ZeroDivisionError
# print('denem'e) --> SyntaxError
# bize gelecek olan bütün hata türlerini tek tek alt seviyelerine inmek kolay olmaz
# genel olarak error denir
################### error handling -> hata yönetimi ####################

# try:
#     x = int(input('x:'))
#     y = int(input('y:')) #kullanıcı y için 0 veya 2a gibi bir değer girerse hata alırız.
#     print(x/y)

# except (ZeroDivisionError,ValueError) as e :
#     print('Yanlış değer girdiniz')
#     print(e) # hatanın çeşidini yazarız
###############################################################
# try:
#     x = int(input('x:'))
#     y = int(input('y:')) #kullanıcı y için 0 veya 2a gibi bir değer girerse hata alırız.
#     print(x/y)

# except:
#     print('Yanlış değer girdiniz')
#     print(e) # hatanın çeşidini yazarız
while True:
    try:
        x = int(input('x:'))
        y = int(input('y:')) #kullanıcı y için 0 veya 2a gibi bir değer girerse hata alırız.
        print(x/y)

    except Exception as exp: #genel hata (base class) tır yukarıdaki  ZeroDivisionError,ValueError genel base class olan 
        #Exception sınnıfından türemişlerdir 
        print('Yanlış değer girdiniz')
        print(exp) 
    else: # except e girmezse else e girer 
        break 
    finally:# try except bloğundan çıktıktan sonra her türlü çalıştırılır try dan hata dönsün veya dönmesin...
        print('try except sonlandı')
    