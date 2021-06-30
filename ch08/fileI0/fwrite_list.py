f = open('C:/pyfile/2021kbo.txt', 'w')
team = ['기아', '삼성', 'LG', 'NC', '키움', 'KT', 'SSG', '롯데']

for i in team:
    f.write(i + " ")
f.close()

'''
# range() 함수
n = len(team)
for i in range(n):
    f.write(team[i] + " ")
f.close()
'''
f = open('C:/pyfile/2021kbo.txt', 'r')
data = f.read()
print(data)
f.close()
