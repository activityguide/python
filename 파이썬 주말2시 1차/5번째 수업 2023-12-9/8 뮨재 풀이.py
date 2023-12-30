# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
# for idx, item in enumerate(colors):
#     print(f'{idx +1}번째 색깔은 {item}')

print("점수를 입력\n더 이상 점수가 없으면 음수를 암거나 입력")
li = []
while True:
    a = int(input('점수를 입력'))
    if a < 0:
        print(f'{round(sum(li) / len(li), 3)}, 최대 {max(li)}, 최소 {min(li)}')
        exit()
    else:
        li.append(a)
