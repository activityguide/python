# 다음은 컴퓨터가 주사위를 던지면 사용자가 주사위의 숫자를 맞추는 프로그램입니다.
# 사용자가 맞힐 때까지 게임은 계속됩니다.
import random

while True:
    a = random.randrange(1, 7)
    b = int(input('주사위 값은 뭘까요~~?>>>>>>>'))
    if a != b:
        print('땡 다시 하세요')
        continue
    else:
        print('맞음')
        break
