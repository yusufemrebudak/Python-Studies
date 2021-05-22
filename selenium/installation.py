# driver dosyam çalıştığım py dosyaları ile aynı dizin içinde 
# kütüphanenin belirttiğimiz web sitesini bir tarayıcı içerisinde açması lazım bunun için bir driver lazım 
# driver da hangi tarayıcıyla çalışacağımızı belirten bir exe dosyasıdır.
# bir web sitesini ziyaret edip yapabilecek olduğumuz tüm işlemleri selenium aracılığıyla yapabiliyoruz.
# şu sayfaya gir kayıt ol ordan çık formu doldur gibi
from selenium import webdriver
driver = webdriver.Chrome()
url = "http://akumburada.com"
driver.get(url) # bir sayfanın açılmasını bu şekilde sağlayabiliriz.