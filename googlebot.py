from config import keys
from selenium import webdriver
import time
def order(k):
    driver = webdriver.Chrome('./chromedriver')

    driver.get(k['product_url'])

    #Click add to cart and wait one second for javascript to load
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(1)
    
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    driver.find_element_by_xpath('//*[@id="order_email"]')
    driver.find_element_by_xpath('//*[@id="order_tel"]')
    #Address
    driver.find_element_by_xpath('//*[@id="bo"]')
    #APT, UNIT, ETC
    driver.find_element_by_xpath('//*[@id="oba3"]')
    #ZIP
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]')
    #C
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]')
    driver.find_element_by_xpath('//*[@id="orcer"]')

if __name__ == '__main__':
    order(keys)

