# 로또 추천 프로그램은 당첨번호가 총 6개가 나온다. 1~
import random
import time
a = random.sample(range(1, 46), 6)
ti = 0
while ti < 6:
    print(f'{ti+1}번째 당첨번호는 {a[ti]}')
    ti += 1
    time.sleep(0.2)
print(f' 당첨번호는 {a}임')
