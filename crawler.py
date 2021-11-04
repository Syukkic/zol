import requests
from bs4 import BeautifulSoup as bs4
from headers import headers
from random import choice
from lxml import etree


class Zol():

    def __init__(self) -> None:

        self.url = 'https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_9_2_0_%i.html'

        self.header = {
            'User-Agent': str(choice(headers))
        }
    
    def fetch_html_page(self):
        page = requests.get(self.url % 1, headers = self.header).text
        return page
    
    def parse(self, page):
        soup = bs4(page, 'lxml')
        # print(soup)
        phone_list = soup.find("ul", class_ = 'clearfix').find_all('h3')
        
        print(len(phone_list))




# /html/body/div[5]/div[1]/div[4]