# 브레이크 문
# whlie 문이나 for 문과 같은 반복문을 강제적으로 종료하고자 할때 사용하는 제어문
# 반복문 내에 break문이 나타나면 곧바로 break문이 포함된 반복문이 종료

n = 1
while n <= 10:
    print(n)
    n += 1
print(n)

print()

n = 2
while True:
    print(n)
    if n == 10:
        break # if 문에서 break문을 작성했지만 실제로 종료하는 건 whlie 문
    n += 1
print(n)
