import re
# bu modul genel olarak bir arama sonucu sonuç döndürür.
result = dir(re)
#print(result)
# ['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'Match', 'Pattern', 
# 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__',
#  '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cache',
#   '_compile', '_compile_repl', '_expand', '_locale', '_pickle', '_special_chars_map', '_subx', 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 
# 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'template']
 
################### # re module

str="Python Programlama Kursu:Python eğitim rehberi | 40 saat"
result=re.findall("Python",str)
print(result) # ['Python', 'Python'] 2 yerde buldu ve liste olarak döndü
result=re.split(" ",str)
print(result) # ['Python', 'Programlama', 'Kursu:Python', 'eğitim', 'rehberi', '|', '40', 'saat', ''] her boşluğa göre stringi list olarak bölmelere ayırır
result=re.sub(" ","-",str)
print(result) # Python-Programlama-Kursu:Python-eğitim-rehberi-|-40-saat-
result=re.search("Python",str)
print(result) # bir match objesi döner  <re.Match object; span=(0, 6), match='Python'> 

# match objesinin span özelliği vardır 0 dan başladık 6 da bulduk diyor.
# result=result.span()
# print(result) # (0, 6) kaçıncı indekste olduğunu söyler yani konumunu alabiliriz.
# result = result.start()
# print(result) # 0 yazar
# result = result.start()
# print(result) # 6 yazar


 #regular expression --> nasıl yazıldığı kendimizde yazabiliyor olmamız lazım

#result = re.findall("[abc]",str) # ['a', 'a', 'a', 'b', 'a', 'a'] yapar
# result=re.findall("[sat]",str) #  ['t', 'a', 'a', 'a', 's', 't', 't', 's', 'a', 'a', 't'] yapar 
# result=re.findall("[a-k]",str) # ['h', 'g', 'a', 'a', 'a', 'h', 'e', 'i', 'i', 'e', 'h', 'b', 'e', 'i', 'a', 'a'] 
# # a dan k ya kadar olan karakterleri aramış oluruz.
# result=re.findall("[0-5]",str) # ['4', '0'] döner 0 dan 5 e kadar rakamları arar.
# [^abc]->abc dışındaki karakterler 
# [^0-9]->rakam harici tüm karakterleri bulur

#^a -> gönderilen stringin ilk kelimesindeki karakter a ile başlıyor mu 
result = re.findall("^P",str)
print(result)

# a$ -> verdiğimiz stringin son karakteri a mı 
result=re.findall("t$",str)
print(result) # ['t'] # döner
result=re.findall("saat$",str)
print(result) # ['saat'] döner
