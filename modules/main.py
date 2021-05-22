import mod
# result = help(mod)
# print(result)
result = mod.numbers
print(result) # [1, 2, 3] 
result = mod.number
print(result) # 10 
result= mod.person['name']
print(result)   # Yusuf
mod.func(10)
p=mod.Person()
p.speak()