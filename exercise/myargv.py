import sys

args = sys.argv[1:] #리스트형 자료
#print(args)
sum = 0
for i in args:
    sum += int(i)

print(sum)