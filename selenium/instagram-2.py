from instaUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome("C:/Users/yusuf/Desktop/python_temelleri/selenium/chromedriver.exe")
        self.username = username
        self.password = password
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)  
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()
        time.sleep(3)



    def get_followers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").click()
        
        time.sleep(2)
        dialog = self.browser.find_element_by_css_selector("div[role=dialog]")
        dialog_1 = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        follower_count = len(dialog_1.find_elements_by_css_selector("li"))
        print(f"First count : {follower_count}")
        action = webdriver.ActionChains(self.browser)
        
        while True:
            dialog.click()    
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            
            time.sleep(2)
            new_count = len(dialog_1.find_elements_by_css_selector("li"))
            if follower_count != new_count:
                follower_count = new_count
                print(f"new cound : {follower_count}")
                time.sleep(1)
            else:
                break
              
        followers = dialog_1.find_elements_by_css_selector("li")
        follower_list = []
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            follower_list.append(link)

        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in follower_list:
                file.write(item+"\n")
        


    # def follow_user(self,username):
    #     self.browser.get("https://www.instagram.com/"+username)
    #     time.sleep(2)
    #     follow_button = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button")
    #     follow_button.click()
        
        


instgrm = Instagram(username,password)
instgrm.signIn()
time.sleep(2)
instgrm.get_followers()
#instgrm.follow_user("kod_evreni")