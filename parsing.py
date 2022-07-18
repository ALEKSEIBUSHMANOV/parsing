KEYWORDS = ['дизайн', 'фото', 'web', 'python']

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# UserAgent().chrome
from user_agents import parse

ua_string = """Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 
(KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3"""
user_agent = parse(ua_string)

Headers = {'User-Agent': UserAgent().chrome}

base_url = 'https://habr.com/ru/all/'
responce = requests.get(base_url, headers=Headers)
text = responce.text
soup = BeautifulSoup(text, 'html.parser')

articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    titles = article.find('a', class_='tm-article-snippet__title-link').text
    date = article.find('time').text
    title_link = article.find('a', class_='tm-article-snippet__title-link').get("href")

    for words in KEYWORDS:
        if words.lower() in titles.lower():
            result = f' Дата <{date}> - Заголовок <{titles}> - Ссылка <{base_url + title_link}>'
            print(result)
