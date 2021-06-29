# 영어 단어 저장하기

f = open("words.txt", 'a')
word = ['sky', 'sea', 'earth', 'moon', 'tree', 'flower', 'grape', 'strawberry', 'garlic', 'potato']
for i in word:
    f.write(i + ' ')
f.close()