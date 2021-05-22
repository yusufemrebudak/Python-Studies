def not_hesapla(satir):
    satir=satir[:-1]
    liste = satir.split(':')
    ogrenci_adsoyad=liste[0]
    notlar=liste[1]
    notlar=notlar.split(',')
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ortalama = (not1+not2+not3) /3
    if ortalama>=90 and ortalama <=100:
        harf='AA'
    elif ortalama >=80 and ortalama <=89:
        harf ='BA'
    elif ortalama >=65:
        harf='CC'
    else :
        harf ='FF'
    return ogrenci_adsoyad+":"+ harf +"\n"

def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding='utf-8') as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad=input('öğrenci adı: ')
    soyad=input('öğrenci soyad: ')
    not1=input('1.Not: ')
    not2=input('2.Not: ')
    not3=input('3.Not: ')
    with open("sinav_notlari.txt","a",encoding='utf-8') as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+','+not3+'\n')
        
def not_kayitet():
    with open("sinav_notlari.txt","r",encoding='utf-8') as file:
        liste=[]
        for i in file:
            liste.append(not_hesapla(i))
            

        with open("sonuclar.txt","w",encoding='utf-8') as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = int(input('1-Notları Oku\n2-Not gir\n3-Notları kayıt et\n4-Çıkış\n'))
    if islem==1:
        ortalamalari_oku()
    elif islem==2:
        not_gir()
    elif islem==3:
        not_kayitet()
    else:
        break

