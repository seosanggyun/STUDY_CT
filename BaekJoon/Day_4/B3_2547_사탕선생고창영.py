# 각 테스트 케이스에 대해 모두에게 같은 사탕을 나눠줄 수 있으면 YES

# 테스트 케이스의 개수를 입력받음
T = int(input())

# 테스트 케이스의 수만큼 반복문
for a in range(T):
    # 각 케이스는 빈 줄로 구분되어 있음
    blank = input()
    # 학생들이 가져온 사탕의 수를 입력받을 줄의 개수를 입력받음
    N = int(input())
    # 총합을 저장할 변수 초기화
    total = 0

    # 입력받은 줄의 개수만큼 반복
    for b in range(N):
        # 학생들이 가져온 사탕의 수를 입력받으면서 총합에 더함
        total += int(input())

    # 총합이 입력받은 줄의 개수로 나누어 떨어지면 YES
    if total % N == 0:
        print('YES')
    else:
        print('NO')