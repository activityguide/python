# 세트 set
# 비시퀸스 자료형이기 때문에 저장된 요소들 사이에 순서가 없음

# 기본 형식
# for 요소 in { 세트 }   # 세트는 중괄호
# 반복 실행
for item in {'가위','바위','보'}:
    print(item)     # 순서가 없기 때문에 실행 할때마다 랜덤하게 나옴

# 2. dictionary
# key 와 value의 조합이라 다른 자료형과 다른 방식으로 사용
# key만 출력
person = {'name':'amily','age':24,'address':'daegu'}
for item in person:
    print(item)

# 가치 출력
for key, value in person.items():
    print(f'{key}:{value}')

print()
for key in person:
    print(f'{person[key]}')

print()
for key in person:
    print(f'{person.get(key)}')
