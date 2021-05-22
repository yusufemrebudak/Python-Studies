user_a=['Yusuf',20]
user_b=['Kadir',24]
user_c=['Ahmet',26]
print(type(user_a))
users=user_a + user_b +user_c
print(users)
print(users[1])    # print(user_a[1]) '20' basar
users = [user_a,user_b,user_c]  ## liste içinde liste saklıyorum 
print(users[2])    # ekrana ['Ahmet', 26] basar
print(users[0][0])  # ekrana  'yusuf' basar
 
