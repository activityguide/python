while True:# 무한 루프
    city = input("where is capital of the korea")
    city = city.strip() # 문자 옆에서 양쪽 끝에 있는 공백 문자를 제거한다.
    if city == 'seoul' or city == '서울' or city == 'SEOUL':
        print('correct')
        break
    else:
        print('wrong, try again')
        