# 개인 정보의 보안 처리를 위하여 주어진 인수의 일부를 *로
# 바꾸어 반환하는 함수를 만들어서
# 이를 모듈로 저장하는 프로그램입니다.

# 모듈명: my_secure.py -> 여기서 실행되어야 함
# secure_name() 함수: 김철수 -> 김**
# secure_no() 함수: 050630-1234567 -> 050630-1******
# secure_phone() 함수 : 010-9492-4154 -> 010-****-4154

def secure_name(name):
    print(f'{name[0]}**')


def secure_no(personalnumber):
    print(f'{personalnumber[0:8]}******')
    return personalnumber[0:8] + '******'


def secure_phone(phonenumber):
    number = phonenumber.replace(phonenumber[4:8], '****')
    print(number)


secure_name('안철수')
secure_no('050630-3876787')

secure_phone('010-9492-4154')
