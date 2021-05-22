# with open("newfile.txt","r+",encoding='utf-8') as file: # r+ demek hem okuma hemde yazma demek.
#     file.seek(20) # 20.konuma kursor set edilir
#     print(file.write("deneme")) # 20.konumdan itibaren deneme yazar.

# with open("newfile.txt","r+",encoding='utf-8') as file: # r+ demek hem okuma hemde yazma demek.
#     print(file.read())

# with open("newfile.txt","a",encoding='utf-8') as file : # sayfa sonuna eklemek için
#     file.write('\nhamiyet budak')


# sayfa başına güncelleme
# with open("newfile.txt","r+",encoding='utf-8') as file: # r+ demek hem okuma hemde yazma demek.
#     content = file.read()
#     content="Efe Turan\n"+ content
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt","r",encoding='utf-8') as file: # r+ demek hem okuma hemde yazma demek.
#     print(file.read())
# sayfa ortalarında güncelleme
with open("newfile.txt","r+",encoding='utf-8') as file:
    list=file.readlines()
    list.insert(1,'Yılmaz Korkmaz\n')
    file.seek(0)
    # for i in list:
    #     file.write(i)
    # print(list) bu da olur

    file.writelines(list) # hazırlanmış listeyi dosyaya direkt yazma 
with open("newfile.txt","r",encoding='utf-8') as file: # r+ demek hem okuma hemde yazma demek.
    print(file.read())