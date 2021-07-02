from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("https://www.naver.com/")
contents = BeautifulSoup(html, 'html.parser')
div = contents.find('div', {'class':'service_area'})
print(div)
a = div.find('a')
print(a.text)