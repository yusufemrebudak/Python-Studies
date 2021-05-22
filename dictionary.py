# key -> value
# 41-> kocaeli  34->İstanbul

sehirler=['kocaeli','istanbul','bursa']
plakalar = [41,34,16]
print(plakalar[ sehirler.index('bursa') ] )
### fakat ben şunu istiyorum 2 liste üzerinden değil de tek liste üzerinden
#print(plakalar['istanbul']) => 34
#print(plakalar['bursa'])   => 16
plakalar ={'kocaeli':41,'istanbul':34,'bursa':16}
print(type(plakalar))
print(plakalar['istanbul'])
plakalar['ankara']= 6 # dictionary e veri eklemek
print(plakalar)
########################################################################
users={
    'yusufbudak':{
        'age':21,
        'email':'yusufbudak@gmail.com',
        'adress':'bursa',
        'phone': '132213213'
    },
    'kadirbudak':{
        'age':25,
        'email':'kadir@gmail.com',
        'adress':'kemerçeşme',
        'phone':'12321312'
    }
}
print(users['yusufbudak']['age'])
print(users['yusufbudak']['email'])
print(users['yusufbudak']['adress'])
print(users['kadirbudak']['adress'])
print(users['kadirbudak']['age'])

