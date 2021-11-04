from crawler import Zol
from concurrent.futures import ThreadPoolExecutor


if __name__ == "__main__":

    urls = f'https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_9_2_0_{i}.html'

    with ThreadPoolExecutor(50) as t:

        for i in range(1, 101):
            t.submit(Zol().download, urls)

    Zol().storage(data)