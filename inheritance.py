class Person:

    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
        print('Person created')

    def who_am_i(self):
        print('i am a person')
    
    def eat(self):
        print('i am eating')

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.student_number = number
        print('Student created')

    def who_am_i(self):
        print('i am a student') 

    def say_hello(self):
        print('hello i am a student')

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch = branch
    
    def who_am_i(self):
        print(f'i am a {self.branch} teacher')
        

p1 = Person('Ali','Yılmaz') # Person created çalıştı
s1 = Student('Çınar','Turan',525) 
# 12. satır Person created
# 12. satır Student created

print(f'p1--> name:{p1.first_name} , lastname:{p1.last_name}') # p1--> name:Ali , lastname:Yılmaz       yazar
print(f's1--> name:{s1.first_name} , lastname:{s1.last_name} , number:{s1.student_number}') # s1--> name:Çınar , lastname:Turan       yazar

p1.who_am_i() # i am a person
s1.who_am_i() # i am a person student person sınıfının methodlarına sahiptir fakat aynı method stududent sınıfında
#var ise student sınıfındaki person sınıfındaki methodu ezer --> OVERRIDING
p1.eat()
s1.eat()  
s1.say_hello() # hello i am a student yazar ve sadece s1 üzerinden çağırılabilir.

t1 = Teacher('Serkan','Yılmaz','Math')
t1.who_am_i() # i am a Math teacher yazar

#   #   #   #   #   #   #  özel methodlar  #   #   #   #   #   #   #   #   #   #   #   #
class Movie:
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie nesnesi oluşturuldu')
    
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration

m1 = Movie('Recep İvedil','Çağan Irmak',120)
# print(len(m1))  #  object of type 'Movie' has no len() döner yani m1 objesi için bir len methodu yok der.
# onun için gidip movie class ı na len methodu ekliyoruz.
print(len(m1)) # ekrana 120 basar
print(str(m1)) # Recep İvedil by Çağan Irmak yazar movie class ındaki __str__ methodu çalışır
del m1  # m1 objesini silerim
