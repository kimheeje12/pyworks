# 속으로 20초를 세어 맞히는 프로그램

input('엔터를 누르고 20초를 셉니다.')
start = ch06.module.time()

input('20초 후에 다시 엔터를 누릅니다.')
end = ch06.module.time()

et = end - start
print('실제 시간:', et, '초')
print('시간 차이:', abs(et-20), '초')      

