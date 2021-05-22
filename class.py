class Person:

    # class attributes
    adress='no information'
    
    #constructor 
    def __init__(self,name,year):
        #object attributes
        self.name = name
        self.year = year
        print('init methodu çalıştı')

    # instance methods
    def intro(self):
        print('hello  there I am '+self.name)

    # instance methods
    def calculate_age(self):
        return 2020-self.year





person1 = Person('Yusuf',2000) # p1 objesi tanımladım ve Person sınıfındaki tüm attribute ve method lara erişirim
person2 = Person('Kadir',1995)
# print(person1)  # __main__.Person object at 0x017EB220 person tipinde ram de yer tutan bir yaşayan nesne vardır
# print(person2)  # _main__.Person object at 0x0193B220  person tipinde ram de yer tutan bir yaşayan nesne vardır

#access,ng object attributes
print(f'name:{person1.name}  year:{person1.year}  adres:{person1.adress}')
print(f'name:{person2.name}  year:{person2.year}   adres:{person1.adress}')
person1.name ='ahmet' # artık person1 nesnesinin isim attribut ü ahmet oldu
print(person1.name) 
person1.intro() #hello  there I am ahmet
person2.intro() #hello  there I am kadir 
person1.name ='Yusuf'
print(f'adım :{person1.name} ve yaşım:{person1.calculate_age()}') # adım :Yusuf ve yaşım:20 

#    #      #   #   #   #   #   #   #   #   #   #   #   #
class Circle:
    #class object attributes
    pi=3.14

    def __init__(self,yaricap=1): 
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return (2*self.pi*self.yaricap)
    def alan_hesapla(self):
        return (self.pi)*(self.yaricap**2)

daire1 = Circle() #yariccap = 1 olur
daire2 = Circle(4)
print(daire1.cevre_hesapla())
print(daire1.alan_hesapla())
print(daire2.cevre_hesapla())
print(daire2.alan_hesapla())