from datetime import date
import requests
import pandas as pd
from headers import headers
from random import choice
from lxml import etree
from concurrent.futures import ThreadPoolExecutor, as_completed

header = {
            'User-Agent': str(choice(headers))
        }
    
def download(url):

    page = requests.get(url, headers = header).text
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

    return result_list
      
def thread_pool(target, args):
    with ThreadPoolExecutor(50) as executor:
        res = executor.map(target, args)
        return res
        
if __name__ == "__main__":
    
    urls = [f'https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_9_2_0_{i}.html' for i in range(1, 101)]

    data = []
    res = thread_pool(download, args=urls)
    for i in res:
        data.extend(i)
        
    df = pd.DataFrame(data)
    df.to_csv('result.csv', index=False, encoding='utf-8')
