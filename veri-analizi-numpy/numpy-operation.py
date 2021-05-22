import numpy as np
numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)
print(numbers1) # [45 41 64 85 34 96]
print(numbers2) # [28 10 34 29 71 60]
result = numbers1 + numbers2 # iki dizinin aynı indeskler toplanır result listesine atanır
print(result)  
result = numbers1 * numbers2 # iki dizinin aynı indeskler çarpılır result listesine atanır
print(result)  
result = np.sin(numbers1) # dizi elemanlarının sinüsünü alır ve bize verir.
print(result)  # [ 0.01770193  0.37960774 -0.98514626 -0.99388865  0.82682868  0.95637593] 

#hstack iki matrisi yatay olarak birleştirir
mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

# result = np.vstack((mnumbers1,mnumbers2)) # vstack iki matrisi dikey olarak birleştirir
# print(result) 
# result = np.hstack((mnumbers1,mnumbers2)) #hstack iki matrisi yatay olarak birleştirir
# print(result)