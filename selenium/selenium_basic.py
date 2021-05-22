from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "http://github.com"
driver.get(url)
driver.maximize_window()
print(driver.title)
#driver.save_screenshot("github.com-homepage.png") # github.com-homepage.png adlı dosyaya açtığımız web sitesinin ekran görüntüsünü kaydeder.
time.sleep(2)
url = "http://github.com/sadikturan"
driver.get(url)
if "sadikturan" in driver.title:
    driver.save_screenshot("github.com-sadikturan.png")
print(driver.title)
driver.back() #sayfa geri alma
driver.forward()# sayfa ileri alma

time.sleep(2)
driver.close()