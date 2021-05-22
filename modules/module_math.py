# her bir py uzantılı dosya module olarak adlandırılabilir

import math #math modulunu -->module_math.py modulune dahil ettik

value=dir(math)
# print(value)
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 
# 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 
# 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot',
#  'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2',
#   'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 
# 'sqrt', 'tan', 'tanh', 'tau', 'trunc']  yazar math modulunun iççindeki bulunan bütün fonksiyonlar geldi


print(math.sqrt(49)) # 7.0

print(math.factorial(7)) # 5040

print(math.floor(45.6)) # 45  aşağı yuvarlar

print(math.ceil(45.6)) # 46 yukarı yuvarlar


# yöntem 1
import math as islem

print(islem.sqrt(9)) # 3.0 

# yöntem 2
from math import * #hepsini çek * tüm fonksiyonları çekmesibi söyler ,bu yöntemde math. yazmaya gerek yoktur  
print(factorial(5)) # 120
print(sqrt(9)) # 3.0
#yöntem 2.2
from math import factorial,sqrt
print(factorial(5)) # 120
print(sqrt(9)) # 3.0
print(ceil(4.5))
# fakat bu iki methodun dışında herhangi method kullanmaya çalışırsak çalışmaz.