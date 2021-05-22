cars=['Bmw','Mercedes','Opel','Mazda']
result=len(cars)
print(result)   #listede kaç eleman vardır?
#   #   #   #    #    #    #    #     #    #
print('İlk eleman:'+cars[0] + ', Son eleman:'+cars[len(cars)-1])
#   #   #   #    #    #    #    #     #    #
cars[3]='Toyota'
print(cars)
#   #   #   #    #    #    #    #     #    #
result='Mercedes' in cars 
print(result)
#   #   #   #    #    #    #    #     #    #
print(cars[-1]) # en son elemanı basar
print(cars[-2]) #en sondan bir öncekiyi basar
#   #   #   #    #    #    #    #     #    #
result = cars[0:3]
print(result)
#   #   #   #    #    #    #    #     #    #
cars[-2:] = ['Toyota','Renault'] # birden fazla elemanı aynı anda değiştiriyoruz.
print(cars)
#   #   #   #    #    #    #    #     #    #
cars= cars + ['Audi','Nissan']
print(cars[4]) # Audi basar
#   #   #   #    #    #    #    #     #    #
del cars[-1] # nissan elemanı silindi 
print(cars)
#   #   #   #    #    #    #    #     #    # liste elemanlarını tersten yazdırma
result=cars[::-1]
print(result)
#   #   #   #    #    #    #    #     #    #   #   #   #   #    #    #    #    #     #    #
student_a=['Yiğit','Bilgi',2010,[70,60,70]]
student_b=['Sena','Turan',1999,[80,80,70]]
student_c=['Ahmet','Budak',1998,[80,90,95]]
result = student_a[0] #'yiğit bilgisi taşır '
result=student_c[3]  # [80, 90, 95] bilgisi taşır

result=f'{student_a[0]} {student_a[1]} {2020-student_a[2]} yaşında ve not ortalaması { ( student_a[3][0]+student_a[3][1]+student_a[3][2] )/3 }'

print(result)

