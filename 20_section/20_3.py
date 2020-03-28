import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
# BeautifulSoupのオブジェクトを作成するために、
#引数に、html変数とhtmlをパースして欲しいことを伝える"html.parserを追加
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)


