# 로또 번호 생성

import random as r

lotto = []

for x in range(6): #0~5    
    n = r.randint(1, 45)
    if n not in lotto: 
       lotto.append(n)
    # if len(lotto) == 6:
        # break
 
#print(lotto)


lotto2 = []
while len(lotto2) < 6:
    n = r.randint(1, 45)
    if n not in lotto2: 
       lotto2.append(n)
       
print(lotto2)
