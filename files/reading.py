# try:
#     file = open("newfile2.txt","r") # read modunda dosyanın o konumda olması lazım yoksa exception alırız
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı.")
#     file.close()

file = open("newfile.txt","r",encoding='utf-8')
# for döngüsü 
# for i in file:
#     print(i,end="")
# file.close()
# read fonk
content1 = file.read() #dosya read methoduyla okunmaya başlandığında kursor ilk başta yanıp söner ve en sona bakar okur
# bir daha read dediğimizde 20. satır kursor en son geldiğinden hiçbir şey okuyamaz.dosyayı kapatıp tekrar açmamız lazım 
print("içerik 1")
print(content1)

content2= file.read()
print("içerik 2")
print(content2)

file.close()
########################################################################################
file = open("newfile.txt","r",encoding='utf-8')
content=file.read(5) # içeriğin ilk 5 karakterini alır..
content2=file.read(5) # içeriğin 5. karakterinden sonraki ilk 5 karakterini alır
print(content) # Yusuf
print(content2) #  Buda
file.close()
################### READLİNE FONKSİYONU   ############################
#tek bir satır okuma 
file = open("newfile.txt","r",encoding='utf-8')
print(file.readline()) # Yusuf Budak,
print(file.readline()) #  İbrahim Hakkı Budak
file.close()
################### READLİNES FONKSİYONU   ############################
# file = open("newfile.txt","r",encoding='utf-8')
# liste = file.readlines() #her bir satır bilgiyi dizi olarak karşımıza çıkarır.
# print(liste)
# print(liste[0],end="")
# print(liste[1],end="")
# file.close()
################### with bloğu   ############################

with open("newfile.txt","r",encoding='utf-8') as file:
    content = file.read()
    print(content) # dmlkasjdıosu32u423jıowedwe tüm dosya okunur
    file.seek(0) # bir methoda bir konum göndermemiz lazım kursorun konumunu verilen parametre olarak set eder. 
    print(file.tell()) #bana kursor konumunu verir. 28.konumda mesela
    content2 = file.read() 
    print(content2)  # dmlkasjdıosu32u423jıowedwe tüm dosya okunur
    # file.close() buna gerek yok with komutunun yanında tanımlanan objenin yaşam süresi zaten blok bitiminde biter..




