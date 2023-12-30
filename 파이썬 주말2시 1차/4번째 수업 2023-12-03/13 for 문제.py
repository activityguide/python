# 1번 문제
# 1부터 5사잉 ㅢ 모든 정수를 역수 출력
for n in range(5, 0, -1):
    print(n)

# 2번 문제-1
a = int(input("원하는 정수값"))
b = []
for item in range(1, a+1):
    b.append(item)
print(f"1부터 {a}까지의 모든 정수의 합은", sum(b), "이다")

# 2번 문제 -2
a = int(input("원하는 정수값"))
total = 0
for i in range(a+1):
    print(i)
    total = total + i
print(total)

# 3번 문제
print()
h = []
many = int(input(" 몇개 보관 할거"))
for d in range(1, many+1):
    h.append(input(f'{d}번쨰 과일을 입력해라'))
print("입력받은 과일들은", h, "입니다")
