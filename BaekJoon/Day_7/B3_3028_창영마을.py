# 가장 왼쪽 컵에 공 넣어놓고 시작
cup = [1,0,0]
order = input()
for idx in order:
    # A일때
    if idx == 'A':
        #pythonic
        cup[0], cup[1] = cup[1], cup[0]
    elif idx == 'B':
        cup[1], cup[2] = cup[2], cup[1]
    elif idx == 'C':
        cup[0], cup[2] = cup[2], cup[0]
    else:
        print('입력 똑바로 해라')

print(cup.index(1)+1)


