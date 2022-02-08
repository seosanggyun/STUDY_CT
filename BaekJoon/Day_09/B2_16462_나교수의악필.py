
# 올림 내림 반올림 쓰려고 임포트
import math

# 학생의 수 입력받음
N = int(input())
# 바꾼 점수들을 저장할 리스트 초기화
changed_list = []
# 평균을 구하기 위한 총합 초기화
total = 0

# 학생의 수 만큼 반복
for scores in range(N):
    # 점수를 문자열로 입력받음
    Q = input()
    # 문자열에서 0과 6을 9로 바꿈
    Q = Q.replace('0', '9')
    Q = Q.replace('6', '9')
    # 문자열을 정수로 형변환하여 저장
    Q = int(Q)
    # 점수가 100점이 넘으면 100점으로 저장
    if Q > 100:
        Q = 100
    
    # 리스트에 차곡차곡
    changed_list += [Q]

# 리스트 순회해서 평균 구하기
for scores2 in changed_list:
    total += scores2

avg = total / len(changed_list)

## ???????????????????????????????????

if avg - int(avg) >= 0.5: 
    print(math.ceil(avg))
else:
    print(math.floor(avg))

    ## 왜 얘는 되고 round(avg)는 안됨??



