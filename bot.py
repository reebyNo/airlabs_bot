from config import keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def order(k):
    driver = webdriver.Chrome('./chromedriver')

    driver.get(k['product_url'])
    driver.find_element_by_xpath('//*[@id="name"]').click()
    #Wait for javascript to load
    time.sleep(1)
#     driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="name"]').send_keys(k["name"])
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="message"]').send_keys(k["message"])
    driver.find_element_by_xpath('//*[@id="footer"]/div/form/ul/li/input').click()


if __name__ == '__main__':
    order(keys)

