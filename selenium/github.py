from githubUserInfo import username , password
from selenium import webdriver
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.repositorys = []

    def signIn(self):
        self.browser.get("http://github.com/login")
        time.sleep(1)
        self.browser.maximize_window()
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
       
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/input[14]").click()


    def getRepositorys(self):
        self.browser.get(f"https://github.com/{self.username}?tab=repositories")
        time.sleep(1)
        repos=self.browser.find_elements_by_css_selector(".col-12.d-flex .d-inline-block a")

        for repo in repos:
            self.repositorys.append(repo.text)
            
        print(self.repositorys)   

github = Github(username,password)
github.signIn()
github.getRepositorys()
        