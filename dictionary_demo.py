ogrenciler={} #dictionaru sözlük veri tipi
number=input("öğrenci no: ")
name = input("öğrenci ad: ")
surname  = input("öğrenci soyadı: ")
phone = input("öğrenci tel: ")

ogrenciler[number]={  # bir obje tanımlamasıdır 
    'ad':name,
    'surname':surname,
    'telefon':phone
}
###################### yukarısı ve aşağısı aynı işi yapar.
# ogrenciler.update({
#     number: {
#         'ad':name,
#         'surname':surname,
#         'telefon':phone

#     }
# })

number=input("öğrenci no: ")
name = input("öğrenci ad: ")
surname  = input("öğrenci soyadı: ")
phone = input("öğrenci tel: ")

ogrenciler[number]={  # bir obje tanımlamasıdır 
    'ad':name,
    'surname':surname,
    'telefon':phone
}

####################################################

number=input("öğrenci no: ")
name = input("öğrenci ad: ")
surname  = input("öğrenci soyadı: ")
phone = input("öğrenci tel: ")

ogrenciler[number]={  # bir obje tanımlamasıdır 
    'ad':name,
    'surname':surname,
    'telefon':phone
}
print(ogrenciler) # {'100': {'ad': 'yusuf', 'surname': 'budak', 'telefon': '12321312'}} 100 key bilgisine karşılık gelen bir başka obje yani key-value yapısı

ogr_no=input("ogrenci no girin: ")
result=ogrenciler[ogr_no]
print(f"Aradığınız {ogr_no} nolu ogrencinin bilgileri :\n Adı:{result['ad']}, Soyadı:{result['surname']}, number : {result['telefon']}")