from crawler import Zol


if __name__ == "__main__":

    pages = Zol().fetch_html_page()
    result = Zol().parse(pages)

    Zol().storage(result)