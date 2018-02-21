url = "http://dantri.com.vn/"

#1 dl webpage
import urllib.request
from bs4 import BeautifulSoup
opener = urllib.request.urlopen(url)

content = opener.read()

html_file = open("dantri.html", "wb")
html_file.write(content)
html_file.close()
#2 extract ROI

#3 extract news

#create a soup
soup= BeautifulSoup(content, 'html.parser')
# print(soup.prettify())
ul = soup.find('ul', 'ul1 ulnew') #class id
# print(ul.prettify())
news_list = []
li_list=ul.find_all('li')
for li in li_list:
    refh4 = li.find('h4')
    refa = refh4.find('a')
    href = url + refa['href']
    title= refa['title']
    news = {
    "title": title,
    'url': href,
    }
    news_list.append(news)

import pyexcel
pyexcel.save_as(records = news_list, dest_file_name= 'dantri.xlsx')
