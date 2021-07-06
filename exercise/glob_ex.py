import glob

# data를 리스트형으로 반환
data = glob.glob("c:/pyworks/exercise/*.py")
print(data)
print(data[0])
print(data[-1])
for i in data:
    print(i)


