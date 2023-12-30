# 다음은 리스트에 포함된 잘못된 데이터를 모두 제거하는 프로그램이다
# 리스트에 저장된 정상 데이터는 모두 'a' 를 포함한 문자열이며, 그렇지 않는 경우 잘못된 데이터

a_list = ['above', 'cookie', 'app', 'about', 'bisket', 'apple', 'april', 'banana']
for i, item in enumerate(a_list):
    if item.find('a') == -1:
        print(f'{a_list.pop(i)}가 제거됨')
print(a_list)
