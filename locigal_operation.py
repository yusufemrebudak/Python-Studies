#    #     #    #     #    #     #    #     #    #
# x=int(input("Sayı gir : "))
# result=(x>0) and (x<100)
# print(result)
# #    #     #    #     #    #     #    #     #    #
# email,password="yusuf@gmail.com",123456
# girilen_mail=input("Mail gir :")
# girilen_sifre=int(input("Şifre gir: "))

# result= (email==girilen_mail.strip()) and (password==girilen_sifre)
# print(result)
################################## is  operatörü 
x=y=[1,2,3] #x ve y aynı adresi taşır ,bellekte aynı yeri gösterir yani.
z=[1,2,3]
print(x==y) # ayn listeyi gösterdikleri için haliyle listenin içindeki değerler de  aynı olduğu için  true döner 
print(x==z) # x ve z nin bellekte göstermiş olduğu listelere atılan değerker aynı olduğundan true döner.. #DEĞER KARŞILAŞTIRILMASI YANİ
print(x is y) # TRUE DÖNER aynı adresi tutuğ tutmadığını kontrol eder
print(x is z) # FALSE DÖNER aynı değerleri taşımalarına rağmen ,x ve y aynı bellekteki aynı adres yerini göstermedikleri için false döndü
x=[1,2,3,4]
y=[1,2,3,4,5]
print(x is y) # false döner
del y[4] # 4.index silindi
print(x==y) # true döner
print(x is y) # yine false döner
################################## in  operatörü 
x=['banana','apple','grape'] # list
print('banana' in x)
name='Çınar' #karakter dizisi yani string
print('i' in name)