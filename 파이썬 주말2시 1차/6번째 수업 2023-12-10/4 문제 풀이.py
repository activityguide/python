a = input('전화번호를 입력')
b = a.split('-')
print(f'{b[1]}국번')

c = a.index('-')
d = a.index('-', 5)
print(f'{a[c+1: d]}국번')

