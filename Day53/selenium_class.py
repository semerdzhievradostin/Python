from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from web_scraping_class import GetApartments
import time


class Sheet:
    def __init__(self):
        super().__init__()
        self.chrome_options = webdriver.ChromeOptions()
        self.prefs = {"profile.default_content_setting_values.notifications": 2}
        self.chrome_options.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.page_n = 1

    def fill(self):
        #Filling the information in the Google Sheet .
        self.driver.get(url="https://docs.google.com/forms/d/e/1FAIpQLSev1KJNNWe6w_xGSnCgF0MFprVM_ebsjPEoCzLiKPOqFb99Fw/viewform")
        wait = WebDriverWait(self.driver, 60)
        page = f"https://www.imot.bg/pcgi/imot.cgi?act=3&slink=9705b4&f1={self.page_n}"
        getinfo = GetApartments(page)
        getinfo.aparts_info()
        self.addresses = getinfo.apart_address_list
        self.prices = getinfo.apart_price_list
        self.links = getinfo.apart_link_list
        advert = 0
        for address, price, link in zip(self.addresses, self.prices, self.links):
            self.address = address
            self.price = price
            self.link = link
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))).click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))).send_keys(self.address)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))).click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))).send_keys(self.price)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))).click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))).send_keys(self.link)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))).click()
            time.sleep(0.5)
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'))).click()
            advert += 1
            if advert == len(self.links):
                advert - len(self.links)
                self.page_n += 1
                self.fill()
