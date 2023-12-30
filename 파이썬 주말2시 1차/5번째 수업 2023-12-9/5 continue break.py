fruits = ['사과', '수박']
count = 3
while count > 0:
    fruit = input('넣고 싶은 과일')
    if fruit in fruits:
        print('동일한 과일 존재')

        print(f'{count}번 남음')
        continue
    fruits.append(fruit)
    count -= 1
    print(f'{count}번 남음')

print(f'있는 과일은 {fruits}이다')
