# 메소드
# 메소드method란 특정 객체 object가 가지고 있는 함수 function을 의미
# 함수는 독립적으로 호출할 수 있지만, 메소드는 특정 객체를 통해서만 호출 가능

# 함수와 다르게 메소드는 특정 객체 소속이어서, 메소드를 호출하려면
# 특정 객체를 통해서만 호출 가능

# 1. 문자열 메소드
# 문자열 str을 처리하기 위해 많은 메소드를 제공
# 1) format()

# 2) count()
# 문자열 내부에 포함된 특정 문자열의 개수를 반환하는 메소드, 특정 문자가 몇번 썼는지 계산
print()
s = '내가 그린 기린 그림은 목 긴 기린 그림이고, 니가 그린 기린 그림은 목 짧은 기린 그림임'
print(s.count('기린'))

# 인덱스를 지정해서 범위 지정 가능
a = 'best of best'
print(a.count('best', 0))

# 마이너스 인덱스도 가능

print(a.count('best', -7))

# 3) find()
# 문자열 내부에 포함된 특정 문자열을 찾고자 할 때 사용
# 찾고자 하는 문자열이 있으면 해당 문자열이 처음으로 나온 위치 즉 인덱스를 변환

print()
b = 'apple'
print(b.find('p'))
# 찾는 문자열이 없을 때 -1 도출
print(b.find('z'))

# 인덱스를 이용해서 검색할 범위도 지정가능
# 시작할 인덱스를 지정하지 않는 경우에는 문자열의 처음부터 찾고, 시작할 인덱스를 지정하는 경우 지정된 인덱스부터 찾음

c = 'best of best'
print(c.find('best'))
print(c.find('best', 5))

# 4) index()
# find() 메소드와 같음. 사용방법도 같다. 차이점은 문자열이 없을 때 발생
# find() 메소드는 찾는 문자열이 없는 경우 -1 도출, index 메소드는 오류 발생
# print()
# d = 'apple'
# print(d.index('p'))
# print(d.index('z'))

# 5) 대소문자 변환 메소드
# upper : 모두 대문자로 변환
# lower :  모두 소문자로 변환
# capitalize : 첫 글자는 대문자로 변환, 나머지는 소문자

print()
e = 'BEST of best'
print(e.upper())
print(e.lower())
print(e.capitalize())

# 6) join
# 인수로 전달한 반복가능 객체(문자열, 리스크)의 각 요소 사이에 문자열을 포함시켜 새로운 문자열을 만들고 그 결과를 도출

print()
print('-'.join('python'))
print('+'.join(['a', 'b', 'c', 'd', 'e']))

# 포함하는 문자 없이 단순하게 리스트의 요소들을 연결하고자 한다면 빈 문자열 사용

print(''.join(['x', 'y', 'z']))
f = {'a': 'apple', 'b': 'banana'}
print(''.join(f))

# 7) split
# 하나의 문자열을 여러 개의 문자열로 분리해서 저장한 리스트를 변환
print()
g = 'Life is too short'
g2 = g.split()  # 단어로 분리
print(g)
print(g2)

h = '010-9492-4154'
h2 = h.split('-')
print(h2)

# 8) replace()
i = 'Life is too short'
i2 = i.replace('short', 'long')
print(i2)

# 특정 문자열을 제거하기 위한 용도로 사용
h = '010-9492-4154'
h3 = h.replace('-', '')
print(h3)

# 9) 불필요한 문자열 제거 메소드
# 문자열 양 끝에 있는 불필요한 문자열을 제거
# lstrip() : 왼쪽 끝에 있는 불필요한 문자열을 제거
# rstip() : 오른쪽 끝에 있는 불필요한 문자열을 제거
# strip() : 양끝에 있는 불필요한 문자열을 제거
print()
j = '                                                      apple'
print(len(j))
j2 = j.strip()
print(len(j2))

# 공백 문자 이외에 불필요한 문자열을 직접 지정 제거
k = '<head'
k2 = k.lstrip('<')
print(k2)
