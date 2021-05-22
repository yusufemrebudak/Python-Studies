import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
# http request ilgili url ye gönderiyoruz ve json değilde bize html içeriği döndürücek.
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser") # bu çekilen veriyi beatiful soup içine vermeliyiz ki tag larına erişebilelim
#print(html)

liste = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=10) 
# classı lister list olan ilk tbody i al sonra 10 tane tr etiketini al 
count=0
for tr in liste:
    count+=1
    title= tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()") 
    # strip metoduna silinmesini istediğimiz karakterleri veriririz
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    print(f"{count} - {title} - IMDB: {rating} - year: {year}")