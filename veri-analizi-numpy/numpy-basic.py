# pyton listelerle yapılamayan bir çok işlemi numpy kütüphaneleri ile yapabileceğiz
# pytondaki list kavramı numpy daki array kavramına karşılık gelir
import numpy as np # kütüphaneye takma isim verdik


py_list = [1,2,3,4,5,6,7,8,9,10] # py list
np_array = np.array([1,2,3,4,5,6,7,8,9]) # np array i oluşturduk

print(type(py_list)) # <class 'list'>

print(type(np_array)) # <class 'numpy.ndarray'>

py_multi = [[1,2,3],[4,5,6],[7,8,9]] 
np_multi = np_array.reshape(3,3)
print(py_multi) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]] her bir eleman yine bir listeye karşılık gelir

print(np_multi) #[[1 2 3] bir matris oluşturduk 
#  [4 5 6]
#  [7 8 9]]

print(np_array.ndim) #1 boyutlu 
print(np_multi.ndim) # 2 boyutlu bir hale getirdik
print(np_multi[0][2]) # 3 verir

print(np_array.shape) # (9,)
print(np_multi.shape) # (3, 3) 

############### NUMPY ARRAYS ###################

result = np.array([1,3,5,7,9])
print(result) # [1 3 5 7 9]
result = np.arange(1,10)
print(result) # [1 2 3 4 5 6 7 8 9] 
result = np.arange(10,100,4) # 100 dahil değildir
print(result) # [10 14 18 22 26 30 34 38 42 46 50 54 58 62 66 70 74 78 82 86 90 94 98]
result = np.zeros(10)
print(result) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
result = np.ones(10) # 10 tane 1 set et
print(result) # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
result = np.linspace(0,100,5)
print(result) # [  0.  25.  50.  75. 100.]
result = np.linspace(0,5,5)
print(result) # [0.   1.25 2.5  3.75 5.  ]
result = np.random.randint(0,10) # 0 ile 10 arasında rastgele sayı üretir
print(result)
result = np.random.randint(0,10,3) # 0 ile 10 arasında rastgele 3 sayı üretir
print(result) # 3 tane rastgele sayı geldi [7 2 3]

