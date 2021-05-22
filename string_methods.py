message=' hello There.My name is Yusuf Budak'
message = message.upper() # "HELLO THERE,MY NAME IS YUSUF BUDAK" yazar 
message = message.lower() # "hello there,my name is yusuf budak" yazar
message = message.title() # "Hello There,My Name Is Yusuf Budak" yazar
message = message.capitalize() #stringin yalnızca ilk kelimesinin ilk karakterini büyük harfle basar
message = message.strip() # ilk karaktere girilen boşluğu siler
result='merhabalarbenyusufemrebudak'.strip('merka') # habalarbenyusufemrebud <-- baştan ve sondan siler daha fazla silmez
print(result)
message = message.split() # boşluklardan bakarak stringteki kelimeleri bana ayır ve dizi olarak dön
 # --> ['hello', 'there,my', 'name', 'is', 'yusuf', 'budak'] <-- olarak döner.yani stringi bir diziye(array) çevirir
# print(message[2])  # "name " yazar ekrana

message='hello There.My name is Yusuf Budak'
message = message.split('.') # [' hello There', 'My name is Yusuf Budak'] bu şekilde dizi döner
print(message) # ekrana 'My name is Yusuf Budak' basar
message = ' '.join(message) # join metodu dizi şeklinde parçalanan stringi ,diziden -> stringe  geri toparlar aralara da ' ' boşluk bırakır
#print(message) 
# message = '*'.join(message) # join metodu dizi şeklinde parçalanan stringi ,diziden -> stringe  geri toparlar aralara da ' ' boşluk bırakır
 # basar --> hello There*My name is Yusuf Budak <--
print(message)
############### string te yusuf kelimesi var mı yok mu kontrol etmek istiyoruz.
index=message.find('Yusuf') 
print(index) # ekrana 24 basar bulur bulmaz kelimenin ilk karafterinin index nuumarasını döner bulamazsa -1 döner
is_found=message.startswith('h')  # message stringi h ile mi başlıyor
print(is_found)
is_found = message.endswith('m') # false döner çünkü stringin son karakteri m ile değil k ile bitmiştir
print(is_found)

message = message.replace('Yusuf','Emre') # yusuf kelimesinin yerine emreyi yazar
# örneğin url yapımında ö yerine o ekle ü yerine u ekle gibi ' ' yerine '-' ekle gibi şeyler yapabilşrz replace metodu ile
print(message)
message=message.center(50,'*')  # ********hello There My name is Emre Budak*********  böyle bir şey yapar.
print(message)
result=message.count('e') # kaç tane e karakteri vardır
print(result)
result=message.count('ello') # ello ifadesi kaç tane var
print(result)