name = 'Yusuf' #5 karakterli bir bilgi ondan dolayı string(karakter dizisi) deniyor. BU artık bir array dir dizidir yani
#bir string aslında bir karakter dizisidir.
surname='Budak'
age = 21
greeting='My name is '+name+' '+surname + '\nI am '+str(age) +' years old.' 
print(greeting) #age int olduğundan doğrudan böyle yazılmaz yan yana
# yazdırılacak parametrelerin aynı tipten olması lazım
print(name[0]+'   '+name[1]+'  '+greeting[5]) #Y   u  m yazar.
print(len(greeting)) # greeting stringinin karakter uzunluğunu döner
print(greeting[ (len(greeting)) -1 ] ) #n son karakteri döner
print(greeting[3:7]) #3. indeksten başla 7. indekse kadar yaz   -->name<--  yazar
print(greeting[3:])  # 3.indeksten başladım önünü kesmedim sonuna kadar yazdı  -->name is Yusuf Budak I am 21 years old.<-- yazar
print(greeting[:10]) # en baştan başla 10.indekse kadar gel -->My name is <-- yazar
print(greeting[2:40:2]) #2 karakterde bir alır yani birini alır birini almaz --> aei uu uam2 er l <-- yazar 
 
 