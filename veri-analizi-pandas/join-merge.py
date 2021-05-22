import pandas as pd 
# customers = {
#     "customer_id":[1,2,3,4,5],
#     "first_name":['ahmet','salih','yusuf','kadir','ibrahim'],
#     "last_name" :['Yılmaz','Budak','Yıldırım','Ay','Gurbulak'],  
# }
# orders={
#     "order_id":[10,11,12,13],
#     "customer_id":[1,2,3,5],
#     "order_date":["2010-08-12","2010-03-22","2010-07-02","2010-02-23"]
# }
# df_customers = pd.DataFrame(customers)
# df_orders = pd.DataFrame(orders)
# print(df_customers)
# print(df_orders)
# result = pd.merge(df_customers,df_orders,how="inner") # inner join yaparak siparişi olarak bütün müşterileri getirmiş oluyoruz.
# print(result)
# result = pd.merge(df_customers,df_orders,how="left") # tüm müşterileri getir siparişi olsa da olmasa da 
# print(result)
# result = pd.merge(df_customers,df_orders,how="right") # tüm sipariş veren müşterileri çektik 
# print(result)

# customers_A = {
#     "customer_id":[1,2,3,4,5],
#     "first_name":['ahmet','salih','yusuf','kadir','ibrahim'],
#     "last_name" :['Yılmaz','Budak','Yıldırım','Ay','Gurbulak'],  
# }
# customers_B = {
#     "customer_id":[4,5,6,7,8],
#     "first_name":['yağmur','çınar','can','cengiz','bilge'],
#     "last_name" :['Korkmaz','Yılmaz','Çelik','Toprak','Kaya'],  
# }
# df_customers_A = pd.DataFrame(customers_A)
# df_customers_B = pd.DataFrame(customers_B)
# result = pd.concat([df_customers_A,df_customers_B])
# print(result)
# customer_id first_name last_name
# 0            1      ahmet    Yılmaz
# 1            2      salih     Budak
# 2            3      yusuf  Yıldırım
# 3            4      kadir        Ay
# 4            5    ibrahim  Gurbulak
# 0            4     yağmur   Korkmaz
# 1            5      çınar    Yılmaz
# 2            6        can     Çelik
# 3            7     cengiz    Toprak
# 4            8      bilge      Kaya  # iki farklı tabloyu birleştirdi

############### PANDAS OPERATİONS METODLARI YANİ #################################################
data = {
    "column1":[1,2,3,4,5],
    "column2":[20,20,13,42,21],
    "column3":["abc","bca","adse","cbccsa","dae"]

}
df = pd.DataFrame(data)
result = df
result = df["column2"].unique()
print(result) # [10 13 42 21] benzersiz değerleri döner yani sadece bir kez kullanılan
result = df["column2"].nunique()
print(result)  # 4 kaç tane eşsiz biilgi var ise o döner

def kareal(x):
    return x*x

result = df["column1"].apply(kareal) # kolon1 altındaki her değerin karesi alınır
print(result)
df["column4"] = df["column3"].apply(len) # kolon1 altındaki her değerin karesi alınır
print(df)  # 3.kolon altındaki string bilgilerin karakter uzunluğunu döner

result = df.sort_values("column2") # kolon2 deki değerler sıralanır artan şekilde
print(result)
result = df.sort_values("column2",ascending=False) # kolon2 deki değerler sıralanır azalan şekilde
print(result)
data2={
    "ay":['Nisan','Mayıs','Haziran','Nisan','Mayıs','Haziran','Nisan','Mayıs','Haziran'],
    "kategori":["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "gelir":[20,40,13,15,61,12,31,14,12]
}

df = pd.DataFrame(data2)
print(df)
print(df.pivot_table(index="ay",columns="kategori",values="gelir"))