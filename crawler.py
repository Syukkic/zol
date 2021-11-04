import requests
from bs4 import BeautifulSoup as bs4
from headers import headers
from random import choice


class Zol():

    def __init__(self) -> None:

        self.url = 'https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_9_2_0_1.html'
        self.headers = choice(headers)
    
    def fetch_html_page(self):
        r = requests.get(self.url)
        print(r.text)




# /html/body/div[5]/div[1]/div[4]