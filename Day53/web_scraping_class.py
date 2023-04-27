from bs4 import BeautifulSoup
import requests

#Scraping imot.bg and checking apartments in Plovdiv with max price of 130 000 EUR
class GetApartments:
    def __init__(self, page):
        self.web_response = requests.get(page)
        self.web_response.raise_for_status()
        self.apart_page = self.web_response.text
        self.apart_soup = BeautifulSoup(self.web_response.text.encode("ISO 8859-1"), "html.parser")
        self.apart_address_list = []
        self.apart_price_list = []
        self.apart_link_list = []
    def aparts_info(self):
        apart_addresses = self.apart_soup.find_all("a", class_="lnk2")
        apart_prices = self.apart_soup.find_all("div", class_="price")
        apart_links = self.apart_soup.find_all("a", class_="lnk3")
        for apart in apart_addresses:
            self.apart_address_list.append(apart.text)
        for price in apart_prices:
            self.apart_price_list.append(price.text)
        for link in apart_links:
            if not link['href'] == "javascript:;":
                self.apart_link_list.append(link['href'][2:])
