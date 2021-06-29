
try:
    f = open('C:/pyfile/hello.txt', 'r')
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")