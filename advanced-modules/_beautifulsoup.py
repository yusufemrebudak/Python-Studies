
from bs4 import BeautifulSoup
html_doc = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
  <h1>MERHABA DÜNYA</h1>

    <div class="group1">
  <h2>KATOGORİKLER</h2>
        <ul>
            <li>menu1</li>
            <li>menu2</li>
            <li>menu3</li>

        </ul>
    </div>
<div class="group2">
        <h2>KATAGORİLER-3</h2>
        
  <ul>
            <li>menu1</li>
            <li>menu2</li>
            <li>menu3</li>

        </ul>
    </div>

    <div class="group3">
        <h2>KATAGORİLER-3</h2>
        
  <ul>
            <li>menu1</li>
            <li>menu2</li>
            <li>menu3</li>

        </ul>
    </div>

    <a href="https://www.w3schools1.com">Visit W3Schools.com!</a>
    <a href="https://www.w3schools2.com">Visit W3Schools.com!</a>
    <a href="https://www.w3schools3.com">Visit W3Schools.com!</a>

'''


soup = BeautifulSoup(html_doc, 'html.parser')
result = soup.prettify()
result = soup.head
result = soup.title  # <title>Document</title>
result = soup.title.name  # title geldi
result = soup.title.string  # Document geldi
result = soup.h1  # <h1>MERHABA DÜNYA</h1>
result = soup.h2  # <h2>KATOGORİKLER</h2>  ilk h2 yi getirir.
result = soup.h2.string  # KATOGORİKLER gelir
result = soup.h3.text
# [<h2>KATOGORİKLER</h2>, <h2>KATAGORİLER-2</h2>] 2 h2  yi de getirir.
result = soup.find_all('h2')
result = soup.find_all('h2')[0]  # <h2>KATOGORİKLER</h2>
result = soup.find_all('h2')[1]  # <h2>KATAGORİLER-2</h2>

result = soup.div  # <div>
# <h2>KATOGORİKLER</h2>
# <ul>
# <li>menu1</li>
# <li>menu2</li>
# <li>menu3</li>
# </ul>
# </div> ilk div geldi
result = soup.find_all('div')[1]  # <div>
# <h2>KATAGORİLER-2</h2>
# <ul>
# <li>menu1</li>
# <li>menu2</li>
# <li>menu3</li>
# </ul>
# </div> 2.div gelir

result = soup.find_all('div')[1].ul  # <ul>
# <li>menu1</li>
# <li>menu2</li>
# <li>menu3</li>
# </ul> 2.div in altındaki ul gelir
# [<li>menu1</li>, <li>menu2</li>, <li>menu3</li>]
result = soup.find_all('div')[1].ul.find_all('li')

result = soup.div.findChildren()  # ilk div in altındaki herşeyi getirir
result = soup.div  # ilk divi getirir
result = soup.div.findNextSibling()  # <div class="group2">
# <h2>KATAGORİLER-2</h2>
# <ul>
# <li>menu1</li>
# <li>menu2</li>
# <li>menu3</li>
# </ul>
# </div> 2.divi döner

result = soup.div.findNextSibling().findNextSibling()  # <div class="group3">
# <h2>KATAGORİLER-3</h2>
# <ul>
# <li>menu1</li>
# <li>menu2</li>
# <li>menu3</li>
# </ul>
# </div>
result = soup.div.findNextSibling().findNextSibling(
).findPreviousSibling()  # <div class="group2">
# <h2>KATAGORİLER-3</h2>
# <ul>
# <li>menu1</li>
# <li>menu2</li>
# <li>menu3</li>
# </ul>
# </div> 2 ye geri döner

result = soup.find_all('a')  # tüm a etiketleri liste şeklinde gelir
for link in result:
    print(link)  # <a href="https://www.w3schools1.com">Visit W3Schools.com!</a>
# <a href="https://www.w3schools2.com">Visit W3Schools.com!</a>
# <a href="https://www.w3schools3.com">Visit W3Schools.com!</a>
for link in result:
    print(link.get('href'))  # https://www.w3schools1.com
# https://www.w3schools2.com
# https://www.w3schools3.com
