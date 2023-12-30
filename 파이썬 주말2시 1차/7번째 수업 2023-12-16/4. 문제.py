money = 9000
# 나이를 입력받아 19세 이상이면 1250원, 13- 18: 1050원, 7- 12: 650원, ~6: 0원
# 잔액은 ...입니다
age = int(input('니 나이'))
if age >= 19:
    print(f'남은 돈은 {money - 1250}원 임돠')
elif age >= 13:
    print(f'남은 돈은 {money - 1050}원 임돠')
elif age >= 7:
    print(f'남은 돈은 {money - 650}원 임돠')
else:
    print(f'닌 공짜임 \n 남은 돈은 {money}원 임돠')

input_number = int(input('아무 정수나 얘기하삼'))
if input_number % 2 != 0:
    print('니가 적은 건 홀수임')
else:
    print('니가 적은 건 짝수 임')

want_low = int(input('원하는 구구단 단을 얘기 하삼'))
count = 0
while count < 9:
    print(f'{want_low} X {count +1} = {want_low*(count+1)}')
    count += 1

li = []
while True:
    b = int(input('원하는 정수를 적으삼 \n 음수를 적으면 종료하삼'))
    if b <= 0:
        break
    li.append(b)
print(f'니가 적은 수중 가장 큰 수는 {max(li)}임돠')

c = int(input('원하는 별 개수 만큼 숫자를 적으삼'))
count_2 = 0
while count_2 <= c:
    e = '*' * count_2
    print(e)
    count_2 += 1
