# 평균이 넘는 사람의 백분율 소수점 셋째자리까지 출력

# 테스트 케이스의 개수 C를 입력받음
C = int(input())

# 테스트 케이스의 수만큼 반복문을 돌면서
# 학생의 수와 점수를 공백으로 구분하여 리스트로 입력받음
for a in range(C):
    N = list(map(int, input().split(' ')))

# 총합과 카운트 초기화
    total = 0
    count = 0
# 점수들의 평균을 구하기 위해 총 합과 점수의 갯수를 구함
# 슬라이싱을 사용하여 리스트 맨 앞의 학생의 수 제외
    for b in N[1:]:
        total += b
        avg = total / (len(N) - 1)

# 평균보다 높은 점수의 갯수를 구함
    for c in N[1:]:
        if c > avg:
            count += 1

# 결과값에 평균보다 높은 점수의 갯수 / 점수의 갯수를 백분율로 저장
    result = count / (len(N) - 1) * 100

# 소수점 셋째자리까지 출력
    print('{:.3f}%'.format(result))
