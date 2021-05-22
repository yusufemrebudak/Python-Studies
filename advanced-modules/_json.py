import json

# person_string='{"name":"Ali","languages":["Python","C#"]}'  # --> string json bilgisi
# #herhangi bir kaynaktan string json bilgisini alıp python içersinde dic yapısına çevirmem lazım
# result = json.loads(person_string)
# print(result) # {'name': 'Ali', 'languages': ['Python', 'C#']} dic ye çevirdik
# print(type(result)) # <class 'dict'>
# result = result["name"]
# print(result) # Ali

########
person_string='{"name":"Ali","languages":["Python","C#"]}'
person_dict={"name":"Ali" , "languages":["Python","C#"]}

# result = json.dumps(person_dict) # dic to json çevirme
# print(type(result)) # <class 'str'>
# print(result) # {"name": "Ali", "languages": ["Python", "C#"]} string olarak yazar

# with open("person.json","w") as f:
#     json.dump(person_dict,f)



# #################  json stringi json objeye çeviririm  ###############333
# result = json.loads(person_string) 
# print(result["name"]) # Ali




# ################# json objeyi stringe çeviririm ###############333
# result = json.dumps(person_dict) 
# print(type(result)) # <class 'str'> 
# # hata verir print(result["name"]) 


