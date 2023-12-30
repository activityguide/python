# n = int(input("정수를 적어라"))
# while n > 0:
#     print(f'{n}번째 hello' )
#     n = int(input("정수를 적어라"))

n = int(input("정수를 적어라"))
if n >= 0:
    while n > 0:
        n = n
        print(n, "번째 hello")

else:
    print("잘못된 값")
