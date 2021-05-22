import pandas as pd 
data = pd.read_csv("all_seasons.csv")
df = pd.DataFrame(data)
print(df.columns)
print(df.head(10))
print(len(df.index)) # 11145
print(df[ df["player_height"] == df["player_height"].max() ] [["player_name","player_height"]])
result = df[ (df["age"]>20) & (df["age"]<25) ][["player_name","team_abbreviation","age"]]
print(result) 
result = df[df["player_name"] == "Matt Mooney"]["team_abbreviation"].iloc[0]
print(result) # CLE yazar 

result = df.groupby("team_abbreviation").mean()[["age","player_height"]]
print(result) # takımlara göre maaş ve boy ortalamalarını verir
result = len(df.groupby("team_abbreviation"))
print(result) # 36 # takım sayısını verir
result = df.groupby("season")["pts"].max()
print(result)
x = df[df["season"]=="2019-20"]
x = x[x["pts"]==x["pts"].max()]
print(x[["player_name","team_abbreviation","age","pts"]])
