months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for month, day in enumerate(months):
    print(f'{month + 1}월은 {day}일까지 이다')

month = 1
for item in months:
    print(f'{month}월 = {item}일')
    month += 1

print()
months_eng = ['jan', 'feb', 'mar', 'apr', 'may', 'jan', 'jul', 'aug', 'sep', 'oct', 'nov', 'decem']

for idx, day in enumerate(months):
    print(f'{months_eng[idx]} = {day}일')
