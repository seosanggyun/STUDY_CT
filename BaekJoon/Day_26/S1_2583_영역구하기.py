from pprint import pprint

M, N, K = map(int, input().split())

arr = [[0 for _ in range(N)] for _ in range(M)]     # 모눈종이
dx = [-1, 0, 1, 0]                                  # 델타
dy = [0, -1, 0, 1]
nerby = []                                          # 넓이를 담을 리스트

for i in range(K):
    x1, y1, x2, y2 = map(int,input().split())       # 좌표 입력

    for j in range(y1, y2):                         # y와 x를 바꿔야
        for k in range(x1, x2):                     # 2차원배열 깔끔하게 들어감
            arr[j][k] = 1

    pprint(arr)

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:                  # 2차원 배열 돌면서 0 찾고
            area = 1                        # 0을 찾으면 넓이 1로 초기화
            arr[i][j] = 1                   # 0을 1로 바꿔서 다음에 검색 안되게
            Q = []                          # BFS를 위한 Q
            Q.append((i,j))                 # Q에 초기좌표 추가
            while Q:                        # Q에 좌표들이 있을 때
                x, y = Q[0][0], Q[0][1]     # x, y 좌표
                Q.pop(0)                    # 좌표 꺼내주고
                for k in range(4):          # 델타 탐색 돌면서
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                        arr[nx][ny] = 1     # 다음 지역이 0이고 범위 내에서만
                        area += 1           # 1 로 바꿔주고 넓이 +1
                        Q.append((nx,ny))   # 다음좌표 Q에 추가
                                               
            nerby.append(area)              # 넓이 리스트에 넓이 추가

print(len(nerby))                           # 넓이 리스트의 길이가 곧 지역 개수
nerby.sort()
for i in nerby:
    print(i, end=' ')