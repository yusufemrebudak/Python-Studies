import json
import os
class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

    pass

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedin = False
        self.currentUser={}
        #load users from .json file
        self.loadUsers()
    
    #json bilgileri uygulama tarafında okunabilir bilgiye çevirip kullanabiliriz.
    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user) #json  string bilgiden bir python objesine çeviririz
                    newUser = User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser)
            print(self.users)
        

    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu")

    def login(self,username,password):
        for user in self.users:
            if user.username==username and user.password==password:
                self.isLoggedin=True
                self.currentUser=user
                print("login yapıldı")
                break

    def logout(self):
        self.isLoggedin=False
        self.currentUser={}
        print("Çıkış yapıldı")

    def identity(self):
        if self.isLoggedin:
            print(f'username:{self.currentUser.username}'
            )
        else:
            print("Kullanıcı giriş yapmadı")
        
    def savetoFile(self):
        liste=[]
        for user in self.users:
            liste.append(json.dumps(user.__dict__))#önce içerideki objeyi sözlük veri yapısına çeviririz daha sonra ise 
            #list e ekleriz

        with open('users.json','w') as file:
            json.dump(liste,file) # kayıt işlemi , dumps ise kayıt işlemi yapılmaz objeyi kayıt edilebilir
            # json bilgiye çeviriyorduk.


repository = UserRepository()

while True:
    print('Menü'.center(50,'*'))
    secim=input("1-Register\n2-Login\n3-Logout\n4-İdentity\n5-Exit\n6-SEÇİMİNİZ: ")
    if secim=='5':
        break
    else:
        if secim=='1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')
            user = User(username=username , password=password , email=email)
            repository.register(user)
        elif secim=='2':
            username = input('username: ')
            password = input("password: ")
            repository.login(username,password)
        elif secim=='3':
            repository.logout()
        elif secim=='4':
            repository.identity()   
        else:
            print("Yanlış Seçim")