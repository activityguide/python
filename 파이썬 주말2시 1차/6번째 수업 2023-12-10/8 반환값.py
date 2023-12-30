# 반환값
# 함수 호출 결과를 도출(return value)
# 반환값이 있으면 함수 내부에서  return 문을 통해 값을 도출
# 반환값이 없으면 함수 내부에 return 문을 작성할 필요가 없다

def address():
    str = '우편번호12345\n'
    str += '서울시 영등포구 여의도'
    return str
print(address())

def address():
    str = '우편번호12345\n'
    str += '서울시 영등포구 여의도'
    print(str)
print(address()) # 반환값이 없어서 출력이 안됨 None

# 3. 함수의 종료를 위한 return
# 반환값이 있으면 return 문을 사용해 반환, 반환값이 없ㅇ면 return 생략
# 반환값이 없을 때도 return 문을 사용하는 경우 => 함수를 종료시킬 때

print()

def charge(energy):
    if energy < 0:
        print(' 0보다 작은 에너지는 충전할 수 없음')
        return
    print('에너지가 충전 중 입니다')
charge(1)
charge(-1)

print(charge)

def print_charge(fun):
    fun(0)
print_charge(charge)

# 5. 함수안의 함수 선언도 가능

def print_greet(name):
    def get_greet():
        return '안녕하세요'
    print(name + "님 " + get_greet())
print_greet("김철수")



