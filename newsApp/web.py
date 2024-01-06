import requests
from bs4 import BeautifulSoup

class Web:
    def __init__(self):
        self.url = 'https://www.nytimes.com/column/sunday-routine'
        self.source = requests.get(self.url)
        self.soup = BeautifulSoup(self.source.text, 'html.parser')

    def get_articles(self):
         articles = []
         li_elements = self.soup.find('ol', class_='asset-stream').find_all('li', class_='css-18yolpw')
         for li in li_elements:
             article = li.find('div', class_='css-14ee9cx').find('article', class_='css-1l4spti').find('p', class_='css-1pga48a e15t083i1')
       # return articles
             if article:
                 articles.append(article.text)

         for word in articles:
            print(word)



