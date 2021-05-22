# kullanımı --> open(dosya_adı,dosya_erişme_modu)
# "w"(write) --> yazma modunda açmak ,dosyayı konumda oluşturur, eğer dosya var ise içerik silinir yeni girilen değerler yazılır. 
# "a"(append) --> ekleme  var olan verinin üzerine veri ekler , dosya konumda yoksa oluşturulur.
# "x"(create) --> dosya oluşturma , dosya zaten varsa hata verir
# "r"(read) --> okuma , dosya konnumda yoksa hata verir.
#############################################################################################
# file = open("newfile.txt","w") #bir obje döner ve o objeyi file da saklarız. ,dosyayı açtık,aynı dizinde oluşturulur
# print(file)
# file.close() #dosyayı kapattık en son kapatmamız lazım.
#############################################################################################3
# file1=open("C:/Users/yusuf/Desktop/newlife.txt","w") # belirli bir dizinde oluşturmak
# print(file1)
# file1.close() #dosyayı kapattık en son kapatmamız lazım.
################################################################################################
# file = open("newfile.txt","w",encoding='utf-8') # şuan var olan newfile dosyasındaki tüm veri silinir
# #file.write('Yusuf Budak,İbrahim Hakkı Budak') # burada tekrardan yazarız.
# file.close()
################################################################################################
# file = open("newfile.txt","a",encoding='utf-8') # şuan var olan newfile dosyasındaki tüm veri silinir
# file.write('\nİbrahim Hakkı Budak') # burada tekrardan yazarız.
# file.close()
################################################################################################
file =  open("newfile2.txt","x") #dosya zaten var ise hata verir.
