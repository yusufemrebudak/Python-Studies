import requests # bu paket python ile otomatikmen inen paketlerden değildir pypi.org dan paketş indirdik
# bir web sitesine bir isteğin sunulması
import json
result = requests.get("https://jsonplaceholder.typicode.com/todos") # bir web sayfasına istekte bulunduk ve json bilgiyi aldık 
print(result) # <Response [200]> başarılı bir yanıt döndü bana
#result=result.text
# print(result)
# print(type(result)) # <class 'str'> json string bilgi döndü bunun elemalarına erişmek için dic e çevirmek lazım

# {
#     "userId": 8,
#     "id": 149,
#     "title": "animi voluptas quod perferendis est",
#     "completed": false
#   },
#   {
#     "userId": 8,
#     "id": 150,
#     "title": "eos amet tempore laudantium fugit a",
#     "completed": false
#   },
#   {
#     "userId": 8,
#     "id": 151,
#     "title": "accusamus adipisci dicta qui quo ea explicabo sed vero",
#     "completed": true
#   },
#   .
#   .
#   .# upuzun geldi

result=json.loads(result.text) #string json bilgiyi list-dic e çevirdik
print(result[1]["title"]) # quis ut nam facilis et officia qui    yazar
for i in result:
    print(i["title"])