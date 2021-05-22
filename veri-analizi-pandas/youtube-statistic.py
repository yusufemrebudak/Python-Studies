import pandas as pd 
data = pd.read_csv("CAvideos.csv")
df = pd.DataFrame(data)
print(df.head())
print(df.columns) # kolon isimleri yazar 
print(len(df.columns)) # 16
df = df.drop("video_error_or_removed",axis = 1)
print(df.columns)
result = df["likes"].mean()
print(result) # 39582.68824148137
result = df["dislikes"].mean()
print(result) #2009.1954453168953 döner
result = df[["likes","dislikes"]].head(10)
print(result)
result = df[df["views"]==df["views"].max()]
print(result[["title","trending_date","views"]])
result = df[df["views"]==df["views"].min()]
print(result[["title","trending_date","views"]])
result = df.sort_values("views",ascending=False).head(5)[["title","views"]] # en fazla görüntğlenen ilk 10 video
print(result)
result = df.groupby("category_id").mean().sort_values("likes")["likes"]
print(result)
result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]
print(result)
print("*"*50)
result = df["category_id"].value_counts()
print(result)
df["title_len"] = df["title"].apply(len)
print(df["tags"])
df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))
print(df)



def like_dislike_oran_hesapla(dataset):
    likes_list = dataset["likes"]
    dislikes_list = dataset["dislikes"]
    tupl_liste =list(zip(likes_list,dislikes_list)) # iki listedeki aynı indeskteki elemanlar [(10,20),(120,30)} şeklinde gelir
    oran_list = []
    for like,dislike in tupl_liste:
        if (like+dislike) == 0:
            oran_list.append(0)

        else:
            oran_list.append(like/(like+dislike))
    return oran_list


df["begeni_orani"] = like_dislike_oran_hesapla(df)
print(df.sort_values("begeni_orani",ascending = False)[["title","likes","begeni_orani"]])