# 주민등록번호 생년월일 6자리 추출
# 사용자로 부터 하이폰을 포함한 전체 주민등록 번호를 입력받아 처리
# 만약 하이폰의 위치가 옯바르지 않으면 오류 메세지를 출력하고 다시 입력하도록 하라

# a = input('하이폰을 포함하여 전체 주민등록번호를 입력하세요.')
# a.find('-')
while True:
    a = input('하이폰을 포함하여 전체 주민등록번호를 입력하세요.')
    if a.find('-') != 6:
        print('다시 입력바람')
        continue
    birthday = a.split('-')
    print(f'{birthday[0]} 니 생년월일')
    break
