import requests
import pandas as pd
from headers import headers
from random import choice
from lxml import etree
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor


class Zol():

    def __init__(self) -> None:

        # self.url = 'https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_9_2_0_%i.html'
        self.header = {
            'User-Agent': str(choice(headers))
        }
    
    # def fetch_html_page(self, urls):
    #     pages = []
    #     for i in range(1, 51):
    #         page = requests.get(self.url % i, headers = self.header).text
    #         pages.append(page)
    #     return pages
    
    def download(self, urls):

        page = requests.get(self.url % i, headers = self.header).text
        html = etree.HTML(page)
        phone_info = html.xpath('/html/body/div[5]/div[1]/div[4]/ul/li')
        result_list = []

        for detail in phone_info:
            detail_dict = {}
            if detail.xpath('./h3/a/text()'):
                detail_dict['name'] = list(filter(None, detail.xpath('./h3/a/text()')))[0].strip()
            if detail.xpath('./div[1]/span[2]/b[2]/text()'):
                detail_dict['price'] = list(filter(None, detail.xpath('./div[1]/span[2]/b[2]/text()')))[0].strip()
            if detail.xpath('./div[2]/span[2]/text()'):
                detail_dict['score'] = list(filter(None, detail.xpath('./div[2]/span[2]/text()')))[0].strip()
            result_list.append(detail_dict)
            
        result_list = list(filter(None, result_list))

        # return result_list
        df = pd.D


    def storage(self, data):
        df = pd.DataFrame(data)
        df.to_csv('result.csv')
