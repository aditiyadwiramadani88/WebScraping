from urllib.request import urlopen as get
from bs4 import BeautifulSoup
import pandas as pd

class ParserUrl:
    def __init__(self, url):
        # raw html
        self.get = get(url).read().decode('utf-8')
    def get_raw(self):
        self.suop = BeautifulSoup(self.get, 'html.parser')
        soup = self.suop 
        # search tag div class price
        self.html_tag = soup.find_all('div', class_='price')
        # search tag div class product_list_title
        self.html_tag2 = soup.find_all('div', class_='product_list_title')
        return self

data = []
url = ParserUrl('http://www.bukabuku.com/').get_raw()
for p, h in zip(url.html_tag2, url.html_tag):
     data.append([p.find('a').string, h.string])

my_df = pd.DataFrame(data)
#then exported to csv
my_df.to_csv('my_csv.csv', index=False, header=False)