from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("https://www.naver.com/")
contents = BeautifulSoup(html, 'html.parser')
ul = contents.find('ul', {'class':'list_nav type_fix'})
#print(ul)
lis = ul.find_all('li')
for li in lis:
    a = li.find('a')
    print(a.text)

    