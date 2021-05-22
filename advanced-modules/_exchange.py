import json
import requests

api_url = "https://api.exchangeratesapi.io/latest?base="
bozulan_doviz=input("bozulan doviz türü: ")
alinan_doviz_turu=input("Alınan doviz türü: ")
miktar=int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz"))

result=requests.get(api_url+bozulan_doviz)
result=json.loads(result.text) #string json bilgiyi list-dic e çevirdik
result=result["rates"]
print(result)

print(f"1 {bozulan_doviz} = {result[alinan_doviz_turu]} TRY")
total = float(result[alinan_doviz_turu]) * miktar
print(f"{miktar} {bozulan_doviz} = {total}")

