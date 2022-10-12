import json
import time
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get('https://annapurnapost.com/search/news?query=%E0%A4%89%E0%A4%AE%E0%A5%8D%E0%A4%AE%E0%A5%87%E0%A4%A6%E0%A4%B5%E0%A4%BE')
content = driver.page_source
fetch_news = []
paged_news={}
time.sleep(15)
soup = BeautifulSoup(content)
all_news=soup.find('div',attrs={'class' : 'row row-search-news-list'})
for news in all_news.find_all_next('div', attrs={'class': "col-xs-12 col-md-6 col-lg-3"}):
    image_url = news.find("img")["src"]
    printed_news = {"title": news.text, "image_url": image_url}
    fetch_news.append(printed_news)

paged_news={"1": fetch_news}

with open("data.json", "w") as f:
    json.dump(paged_news, f)
driver.close();