#도형 면적 구하기

def square(w, h):
    area = w * h
    return area

def triangle(n, h):
    area = n * h / 2
    return area

print('사각형의 면적: ', square(5, 4))
print('삼각형의 면적: ', triangle(4, 7))
