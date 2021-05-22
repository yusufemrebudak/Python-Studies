from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #enter işlemi için
import time
driver = webdriver.Chrome()
url = "http://github.com"
driver.get(url)
driver.maximize_window()

search_input = driver.find_element_by_name("q")
time.sleep(1)
search_input.send_keys("css")
time.sleep(2) 
search_input.send_keys(Keys.ENTER) # input üzerinden enter tuşuna bastık
time.sleep(3) 
result = driver.find_elements_by_css_selector(".repo-list-item .f4 a")



for item in result:
    
    print(item.text)

driver.close()