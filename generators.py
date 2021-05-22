
# YERDEN TASARRUF ETMEK İÇİN 
 
# def cube():
#     result=[]

#     for i in range(5):
#         result.append(i**3)  ## burada tek ama ekrana sayıları basmak fakat bu , liste büyüdükçe gereksiz bir yer işgaline neden olur
#     return result

# print(cube())

def cube():
    for i in range(20):
        yield  i ** 3    # yield bizim için bir değer üretir ve bana gönderiyor ama hiçbir yerde saklanmıyor , bir daha ulaşamam  
        # bize bir generator gönderir.

# print(cube()) # <generator object cube at 0x019CDBC0>

# generator = cube() # buna gerek bile yok       
# iterator = iter(generator)

# direkt şöyle de yazılabilir
iterator = cube() # kendi içinde generatoru iteratore çevirir.

# print(next(iterator)) # 0 
# print(next(iterator)) # 1 
# print(next(iterator)) # 8 
# print(next(iterator)) # 27 
# print(next(iterator)) # 64


for i in iterator:
    print(i)