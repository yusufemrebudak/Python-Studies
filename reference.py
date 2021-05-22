# value type
x=10
y=20
x=y
y=10
print(x,y) # 20 ve 10 yazar value type lar ayrı ayrı alanlarda değer olaak tutulduğundan y deki değişiklikten x etkilenmez


# referance type --> list
# fakat referans typler da durum value type lardan farklıdır,a üzerinde yaptığım değişiklik b yide etkiliyor burada
# a=b dedikten sonra artık iki list objeside aynı adresi taşır ve aynı adresi gösterir ondan dolayı b[0] dersek artık liste üzerinde yapılan 
#herhangi bir değişiklik aynı adresi gösteren iki obje de de otomatikman  yapılır
# listi tanımladık a artık adreste farklı bir bellek alanını tutan adres tutucudur. atıyorum
# a=0000100 ve b=0000110 idi a=b yaptıktan sonra artık b nin içindeki adres a ya kopyalandı yani ikiside 0000110 oldu
# ikiside 0000110 adresini gösteriyor ondan dolayı b[0] ı değiştirirsek artık ikiside aynı adresi gösterdiğindenn print(a,b) yazdığımda
# b de yapılan değişiklikler ne ise bize onu görürüz.
a=['apple','banana']
b=['apple','banana']
a=b
b[0]='grape'
b.append('ali')
print(a,b)
#