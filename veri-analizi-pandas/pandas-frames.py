import pandas as pd
# serilerde bi kolon ismi yoktur sadece indeksleme vardır
#dataframelerde kolon isimleride mevcuttur
s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1 , oranges = s2) # sözlük veri yapısına verdiğimiz parametreler kolon isimlerine dönüştü
print(data) # {'apples': 0    3
# 1    2
# 2    0
# 3    1
# dtype: int64, 'oranges': 0    0
# 1    3
# 2    7
# 3    2
# dtype: int64}
df = pd.DataFrame(data)
print(df) #  apples  oranges
# 0       3        0
# 1       2        3
# 2       0        7
# 3       1        2
##################################################3
data2 = [['ahmet',50],['kadir',30],['yusuf',60],['salih',40]]
df2 = pd.DataFrame(data2 , index = [1,2,3,4] ,  columns = ['Name','Grade'] , dtype = float) # dtype = float gelen sayısal bilgiler float olarak gelir
print(df2) 
#     Name  Grade
# 1  ahmet     50
# 2  kadir     30
# 3  yusuf     60
# 4  salih     40
dic = {"name":["ali","ahmet","kadir","salih"],"grade":[50,60,70,80]}
df = pd.DataFrame(dic,index=["10","11","12","13"])
print(df)  
#       name  grade
# 10    ali     50
# 11  ahmet     60
# 12  kadir     70
# 13  salih     80

dic_list = [
    {"name":"ahmet","grade":50},
    {"name":"salih","grade":30},
    {"name":"kadir","grade":20},
    {"name":"yusuf","grade":40}
]
df = pd.DataFrame(dic_list , index=["10","11","12","13"])
print(df) 
#    name    grade
# 10  ahmet     50
# 11  salih     30
# 12  kadir     20
# 13  yusuf     40

