# 2. 리스트 메소드
# 1) append()
# 리스트의 끝에 인수로 전달된 데이터를 추가

my_list = ['apple', 'banana']
my_list.append('cheery')
print(my_list)

# 2) extend()
# 리스트에 다른 리스트나 튜플과 같은 반복가능 객체를 추가하여 기존 리스트를 확장
print()
my_list = ['apple', 'banana']
my_list.extend(['cheery', 'mango'])
print(my_list)

my_list = ['apple', 'banana']
my_list += ['cheery', 'mango']
print(my_list)

# 3) inset()
# 리스트의 특정 인덱스(위치)에 데이터를 추가
print()
my_list = ['apple', 'banana']
my_list.insert(0, 'cheery')
print(my_list)

# 4) clear()
# 리스트에 저장된 모든 요소를 삭제
print()
my_list = ['apple', 'banana']
my_list.clear()
print(my_list)

my_list = ['apple', 'banana']
my_list = []
print(my_list)

# 5) pop
# 리스트의 마지막 요소가 도출되면서 삭제
print()
my_list = ['apple', 'banana']
item = my_list.pop()    # pop이라는 함수가 item이라는 인덱스로 바나나를 주고 my_list 함수의 바나나 삭제
print(item)
print(my_list)

# 6) remove()
# 인수로 전달된 값과 동일한 요소를 찾아서 제거, 동일한 요소가 여러 개인 경우에는 첫번째만 제거
print()
my_list = ['apple', 'banana', 'cherry', 'mango']
my_list.remove('cherry')
print(my_list)

my_list = ['apple', 'banana', 'cherry', 'mango', 'cherry']
my_list.remove('cherry')
print(my_list)
