import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        pass
#__init__メソッドはスクレイピング対象になるWEBのURLを受け取る。


import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()

#unrlopen関数はWEBサイトのリクエストを行う。
#response.readメソッドを呼ぶとHTMLデータが、Responseオブジェクトから返す。
