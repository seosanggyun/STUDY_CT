# 조건에 맞는 입력값들 입력받음
R, C = map(int,(input().split()))
A, B = map(int,(input().split()))

# 출력할 때 두가지 타입만 있으면 됨
type1 = ''
type2 = ''

# 열은 C, 열의 넓이는 B
for i in range(C):
    # i가 짝수일 때
    if i % 2:
        type1 += 'X' * B
        type2 += '.' * B
    # i가 홀수일 때
    else:
        type1 += '.' * B
        type2 += 'X' * B

# 행은 R, 행의 넓이는 A
for j in range(R):
    # j가 짝수일 때
    if j % 2:
        for k in range(A):
            print(type1)
    # j가 홀수일 때
    else:
        for k in range(A):
            print(type2)