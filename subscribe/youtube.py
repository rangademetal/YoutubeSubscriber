from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Youtube():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome('/Users/andreistroe/Desktop/chromedriver')
        self.driver.maximize_window()
        self.driver.get('https://www.youtube.com')
        self.username = username
        self.password = password

    def loginYoutube(self):
        click = self.driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a')
        click.click()
        click = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        click.click()
        click.send_keys(self.username)
        click = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
        click.click()
        time.sleep(2)
        click = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        click.click()
        click.send_keys(self.password)
        click = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
        click.click()
    def giveSubscribe(self, arr):
        time.sleep(2)
        for i in arr:
            self.driver.get(i)
            click = self.driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button')
            click.click()
            time.sleep(3)



