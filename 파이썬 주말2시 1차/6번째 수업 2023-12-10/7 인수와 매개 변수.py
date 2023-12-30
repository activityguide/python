# 인수와 매개 변수
# 함수로 전달되는 인수 (argument)를 저장하는 변수를 매개변수 (parameter)라고 한다.

# 1. 인수가 있는 함수

def introduce(name, age):
    print(f' my name is { name }, my age is { age }')
introduce( ' yuseonwu', 19)
introduce(age=19, name='yuseonwu')

def show(*args):
    for item in args:
        print(item)
show('python')
show('happy', 'birthday')

# 3. 디폴트 매개변수
# 매개변수로 전달되는 인수가 없는 경우에 기본적으로 사용
# 매개변수를 기본값으로 설정 가능

print()

def hello(message = '안녕하세요'):
    print(message)
hello()
hello('만나서 반값습니다')

# 디폴트 매개변수가 있는 경우 뒤로 배치

def hello2(name, message='안녕하쇼ㅔ요'):
    print(f'{name}님 {message}')
hello2('yuseonwu')
hello2('yuseonjae', '반갑습니다.')

def hello3(name = '유선우', messahe = '안녕하세요ㅕ'):
    print(f'{name}님 {messahe}')

hello3()
hello3('유선재')
hello3('유선재', '반갑습니다')




