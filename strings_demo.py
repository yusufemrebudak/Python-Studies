website = 'http://www.sadıkturan.com.'
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
#1- 'course ' karakter dizisinde kaç karakter bulunmaktadır?
result=(len(course))
#2- 'website'karakter dizisinin içinde www karakterlerini alın.
result=website[7:10]
#3- 'website'karakter dizisinin içinde com karakterlerini alın.
length = len(website)
result=website[(length-4):(length-1)]

#4- 'course ' karakter dizisinden ilk 15 ve son 15 karakter al?
result=course[:15]
#5- 'course' ifadesindeki karakterleri tersten yazdırın? 
result=course[::-1] 

s='12345'*5 # 5 kere '12345' ifadesini yazar
print(s)
print(s[::5]) # 11111 yazar
######################################################################
name,surname,age,job=('yusuf','emre',21,'muhendis')
result = "Benim adım "+name+" "+surname+",yaşım "+" "+ str(age) + " ve mesleğim "+job #bunu yapmaktansa
result=f"Benim adım {name} {surname} , Yaşım {age} , ve mesleğim {job}" 


result="Benim adım {n} {s} , Yaşım {a} , ve mesleğim {j}".format(n=name,s=surname,a=age,j=job) ## 21,22,23 aynı işi yapar


















print(result)