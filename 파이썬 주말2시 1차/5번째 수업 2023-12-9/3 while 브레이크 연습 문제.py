# 브레이크를 사용
# 사용자로 부터 숫자를 입력받고
# 입력된 숫자가 10보다 크면 반복문이 종료
# 10 보다 작으면 계속 반복

# a = int(input('아무 숫자나 적어봐'))
#
# while a <= 10:
#     a = int(input("다시 아무 숫자나 적어봐"))
#     if a > 10:
#         break
while True:
    a = int(input('아무 숫자나 적어봐'))
    if a > 10:
        print(' 큼 종료함')
        break
    else:
        print('10이하임')