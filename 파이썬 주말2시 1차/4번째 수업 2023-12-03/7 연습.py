# 커피 한잔 300원
# # 돈 넣을 수 있는 커피 잔 과 잔돈함깨
# coffee = 300
# n = int(input("니가 넣을 돈"))
# a = n/coffee
a = int(input("니가 넣을 돈"))
if a < 300:
    print("거지")
else:
    b = 0
    while a>= 300:
        b += 1
        a -= 300
        print(f'커피{b}잔, 잔돈 {a}원')
