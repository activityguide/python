# 8에서 9사이의 정수를 입력
# 받을 수 있는 기회는 5번
# 5번을 받고 나면 ' 모두 입력됨' 입력된 값은 ' ' 입니다
# 제약: 8에서 9사이의 정수를 받지만 같은 정수를 받을 시 하나로 입력

# a = 8
# b = int(input("작동할 정수"))
# c = {}
# d = [c]
# while b == a:
#     if b != a:
#         print("틀림")
#         d.append(b)
#         if d[4] == True:
#             print("모두 입력됨")
#     b = int(input("작동할 정수"))

yourlist = []
a = 1
while a <= 5:
    print(f'총 기회는 {6-a}번 남았슴')
    b = int(input("작동할 정수"))
    yourlist.append(b)
    a += 1
print("모두 입력되었습니다")
print(f'입력된 값은 {yourlist}')
