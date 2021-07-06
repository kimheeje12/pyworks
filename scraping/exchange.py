from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("https://finance.naver.com/marketindex/")
code = html.read().decode('euc-kr', 'replace').encode('utf-8', 'replace')
contents = BeautifulSoup(code, 'html.parser')
ul = contents.find('ul', {'class':'data_lst'})
lis = ul.find_all('li')

for li in lis:
    ex = li.find('span', {'class' : 'blind'}) # 환율 종류
    val = li.find('span', {'class' : 'value'}) # 환율 지수
    #print(ex)
    #print(val)
    print(ex.string.split(' ')[-1], ':', val.string)