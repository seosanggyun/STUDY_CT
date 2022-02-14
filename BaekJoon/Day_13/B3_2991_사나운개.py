# 댕1은 A초 공격, B초 수비
# 댕2는 C초 공격, D초 수비
# 댕댕이들의 공격패턴 입력받음
A, B, C, D = map(int, input().split())

# 트리오의 도착시간 입력받음
arrival_list = list(map(int, input().split()))

# 도착시간을 리스트로 저장


# 댕1의 패턴 총 시간 저장
d1c = A + B
# 댕2의 패턴 총 시간 저장
d2c = C + D

# 도착시간을 for문으로 순회
for time in arrival_list:
    # 카운트 초기화
    count = 0
    
    # 도착시간을 패턴시간으로 나눈 나머지 값이
    # 0보다 크고 공격시간보다 작으면
    # 도착시 그 강아지는 공격하는 시간
    # 공격 시간에 도착할때마다 카운트 +1
    if 0 < time % d1c <= A:
        count += 1

    if 0 < time % d2c <= C:
        count += 1

    print(count)

