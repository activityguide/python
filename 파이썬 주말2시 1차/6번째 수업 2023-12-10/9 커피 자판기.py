# 커피 자판기에 돈과 주문할 커피 전달
# 주문할 수 있는 커피의 종류와 가격
# 아메리카노 1000
# 카페라떼ㅔ 1500
# 카푸치노 2000
menu = {'아메리카노': 1000, '카페라떼': 1500, '카푸치노': 2000}
print(' 아메리카노는 1000원 카페라떼는 1500원 카푸치노는 2000원 ')
# def coffemachine(kind, want_kind, input_money):
#     if kind not in menu:
#         print(" 그런 음료 없음 다시 적으삼")
#         return
#     if input_money < want_kind*menu[kind]:
#         print('니 돈 부족')
#         return
#     print(f'니가 시킨 건 {kind}이고, 니가 시킨 음료 수는 {want_kind}, 니가 넣은 돈은 {input_money}, 남은 돈은 {input_money-(want_kind*menu[kind])}')
#
# coffemachine(input('니가 시킨 음료'), int(input('니가 시킨 음료 수')), int(input('니가 넣을 돈')))

def coffemachine(input_money, want_beverage):
    print(f'{input_money}에 {want_beverage}을 선택')
    menu = {'아메리카노': 1000, '카페라떼': 1500, '카푸치노': 2000}
    if want_beverage not in menu:
        print(" 그런 음료 없음 다시 적으삼")
        return input_money, '없는 메뉴'
    if menu[want_beverage] > input_money:
        print('니가 시킬 수 있는 건 없음')
        return input_money, '돈 부족'
    else:
        return input_money - menu [want_beverage], want_beverage

order = input('니가 선택한 음료')
pay = int(input('니가 넣을 돈'))
change, coffee = coffemachine(pay, order)
print(change)
print(coffee)
print(f'잔돈 {change}, 커피 {coffee}')


