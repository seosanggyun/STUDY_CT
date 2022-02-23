# 커플석이 없으면 사람수만큼 컵홀더를 쓸 수 있음
# 커플석이 있으면, 커플석(짝) 개수 -1만큼의 사람수만큼 컵홀더를 쓸 수 있음

# 사람 수 입력
N = int(input())
# 좌석 입력
seats = input()
# 카운트 초기화
count = 0

# 좌석의 갯수만큼 반복
for i in range(len(seats)):
    # 좌석이 커플석일 경우
    if seats[i] == 'L':
        # 카운트 1 더해줌
        count += 1

# 커플석이 없을 경우
if count == 0:
    # 사람 수만큼 컵홀더 사용 가능
    print(len(seats))
# 커플석이 있을 경우
else:
    # 커플석(짝) 개수 -1 만큼의 사람수만큼 컵홀더 사용 가능
    print(len(seats) - (count//2 - 1))


    


