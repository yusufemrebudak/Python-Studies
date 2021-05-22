# isim=input('isim: ')
# yas=int(input('yas: '))
# egitim=input('Eğitim durumu (universite veya lise): ')
# if (yas>=18) and   (egitim=='universite' or egitim=='lise') :
#     print('Sayın '+isim+' ehliyet alabilirsiniz.')
# else:
#     print('Sayın '+isim+' ehliyet alamazsınız.')
###############################################################
import datetime

tarih=input('aracınız hangi tarihte trafiğe çıktı example(2019/8/9) : ')
tarih = tarih.split('/')
print(tarih)
trafige_cikis = datetime.datetime( int(tarih[0]),int(tarih[1]),int(tarih[2]) ) #tarih objesi hazırladım
simdi = datetime.datetime.now()
fark = simdi - trafige_cikis # ikiside datetime objesi ve ordan da gün bilgisini alıyoruz.
days =fark.days
print(days)
