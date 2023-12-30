a = input('학생 이름과 성적 입력')
b = a.split(',')
c = b[0].strip(' \" ')
d = b[1]
print(f'이름은 {c}이고 성적은 {d}점이다')
