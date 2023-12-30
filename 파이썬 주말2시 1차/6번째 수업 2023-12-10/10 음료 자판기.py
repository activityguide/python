# 700원 음료를 뽑을 수 있는 자판기
# 돈을 넣으면 몇잔 뽑을 수 있는지 잔돈은 얼마인지 경우의 수를 출력


def vendingmachine(money):
    a = money // 700
    b = money % 700
    while a > 0:
        print(f'음료수 {a}개 , 잔돈 {b}원 ')
        a -= 1
        b += 700
vendingmachine(int(input('니가 넣을 돈')))



