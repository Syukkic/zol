from crawler import Zol


if __name__ == "__main__":

    run = Zol()
    page = run.fetch_html_page()
    run.parse(page)