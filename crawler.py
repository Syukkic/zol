import requests
from bs4 import BeautifulSoup as bs4
from headers import headers
from random import choice
from lxml import etree
from pprint import pprint

# https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_9_2_0_1.html
# https://zhuanlan.zhihu.com/p/35326408

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
        # soup = bs4(page, 'lxml')
        # phone_list = soup.find("ul", id = 'J_PicMode').find_all('li > data-follow-id')
        # pprint(phone_list[:3])
        html = etree.HTML(page)
        # content = etree.tostring(html, encoding='utf-8')
        # print(content.decode())
        phone_list = html.xpath('//*[@id="J_PicMode"]')

        for phone in phone_list:
            # print(phone)
            title = phone.xpath('//li/h3/a/text()')
            
        # #     # phone_dict['title'] = phone.find('h3').text # .split(' ')[0]
        # #     # phone_dict['price'] = phone.find('span', {'class': 'price price-na'}).find('b', {'class': 'price-type'}).text
        # #     # phone_dict['stars'] = phone.find('span', {'class': 'score'}).text

        #     title = phone.find('h3').text # .split(' ')[0]
        #     price = phone.find('span', {'class': 'price price-na'}).find('b', {'class': 'price-type'}).text
        #     stars = phone.find('span', {'class': 'score'}).text
            
            print(title)
        #     print(price)
        #     print(stars)
        #     break
        # print(phone_dict)