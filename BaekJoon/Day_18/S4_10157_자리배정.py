from pprint import pprint

C, R = map(int, input().split())
K = int(input())

# 가로로 C개의 좌석 = C개의 열
# 세로로 R개의 좌석 = R개의 행
# 좌석들을 둘러싸는 1로 이루어진 테두리도 설정
seats = []
seats.append([-1]*(C+2))
seats += [[-1] + [0] * C + [-1] for _ in range(R)]
seats.append([-1]*(C+2))

# 맨처음 시작할 때 방향
flag = 1

# 시작점의 인덱스 설정
i = R
j = 1

# 대기번호
n = 1

# 만약 대기번호가 R * C(총 좌석 수)보다 클 경우는
# 자리가 없다는 뜻이므로
# 0 출력
if K > R * C:
    print(0)

# 대기번호가 총 좌석 수보다 작거나 같을 경우
else:
    # 시작점 1로 시작
    seats[i][j] = 1

    # 대기번호가 입력받은 K값보다 작을 때에만 실행
    # 즉 대기번호를 넘어서까지는 실행 안하게
    while n < K:
        # 위로 갈때
        if flag == 1:
            # 위쪽 탐색해서 0이면
            # 현재 위치를 한칸 위로 바꾸고
            # 대기번호 +1 해서
            # 대기번호를 현재위치에 저장
            if seats[i-1][j] == 0:
                i -= 1
                n += 1
                seats[i][j] = n
            # 만약 벽을 만나거나
            # 지나온 점을 만나면
            # 오른쪽으로 탐색을 시작할 수 있도록
            # flag 2로 설정
            else:
                flag = 2

        # 오른쪽으로 갈 때
        elif flag == 2:
            if seats[i][j+1] == 0:
                j += 1
                n += 1
                seats[i][j] = n
            else:
                flag = 3

        # 아래로 갈 때
        elif flag == 3:
            if seats[i+1][j] == 0:
                i += 1
                n += 1
                seats[i][j] = n
            else:
                flag = 4

        # 왼쪽으로 갈 때
        elif flag == 4:
            if seats[i][j-1] == 0:
                j -= 1
                n += 1
                seats[i][j] = n
            else:
                flag = 1

    # 반복문이 끝났으면
    # 좌석들 안에 K가 있을거임
    # 그 K의 위치를 탐색한 뒤
    # 좌표를 반환하는데
    # 문제에서 요구하는 좌표는
    # 내가 보통 사용하던 이중배열의 좌표와 좀 다름
    # 문제에서 요구하는 대로 맞춰줘야 함
    # 맞춰 주려면
    # i와 j 순서를 바꾸어서 출력해야 하고
    # i대신 R-i+1을 해야
    # 정답이 나옴     
    for i in range(R+2):
        for j in range(C+2):
            if seats[i][j] == K:
                print(j, end=' ')
                print(R-i+1)
        
    
pprint(seats)


