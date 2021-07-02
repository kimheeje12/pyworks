from urllib import request
from bs4 import BeautifulSoup

def getcontent():
    url = "https://finance.naver.com/item/main.nhn?code=005930"
    html = request.urlopen(url)
    content = BeautifulSoup(html, 'html.parser')
    return content

contents = getcontent()
no_today = contents.find('p', {'class':'no_today'})
print(no_today)
price = no_today.find('span', {'class':'blind'}) #blind는 웹에서 보이지 않음
print(price)
print("삼성전자 주가: {}".format(price.text))