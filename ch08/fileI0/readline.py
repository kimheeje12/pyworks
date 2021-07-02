
with open("2021kbo.txt", 'w') as f:
    team = ['삼성', 'LG', '기아', '롯데']
    for i in team:
        f.write(i + '\n')

with open("2021kbo.txt", 'r') as f:
    # data = f.readlines()    # 파일읽기를 하면 전체 내용을 리스트로 반환
    # print(data)
    # 이차원리스트 만들기
    # d2 = []
    '''
    for i in range(4):
        data = f.readline().split()
        print(data)
    '''

    # 이차원리스트 만들기
    d2 = [] # 새 리스트 준비
    for i in range(4):
        d2.append(f.readline().split())
        print(d2)
