from itertools import count
import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# def count_left_cheese():
#     count = 0
#     for i in range(N):
#         for j in range(M):
#             if pan[i][j] == -1:
#                 count += 1
#     return count

# def cheese_start():
#     for i in range(N):
#         for j in range(M):
#             if pan[i][j] == -1:
#                 return (i,j)


# def bfs():
#     global air, time, cheese
#     Q = deque()
#     start_x, start_y = cheese_start()
#     Q.append((start_x, start_y))
#     visited = [[0 for _ in range(M)] for _ in range(N)]
#     visited[start_x][start_y] = 4
#     while Q:
#         x, y = Q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
#                 if pan[nx][ny] == air:
#                     visited[nx][ny] = 1
#                     Q.append((nx,ny))
#                 elif pan[nx][ny] == -1:
#                     pan[nx][ny] = time
#                     visited[nx][ny] = 1
#     pprint(visited)

#     air += 1
#     time += 1
#     # cheese = time
#     return count




# N, M = map(int, input().split())
# pan = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(M):
#         if pan[i][j] == 1:
#             pan[i][j] = -1


# air = 0
# time = 1


# while True:
#     bfs()
#     pprint(pan)
#     pprint(visited)
#     cheese_left = count_left_cheese()
#     if cheese_left == 0:
#         break

# bfs()
# pprint(pan)
# print(air,time)

# print(cheese_left)

def bfs():
    Q = deque()
    Q.append((0,0))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    count = 0
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 0일 때만, 즉 공기일때만 Q에 추가해줌
                if pan[nx][ny] == 0:
                    visited[nx][ny] = 1
                    Q.append((nx,ny))
                # 1이면 추가 안해줌, 추가했을 시
                # 한번에 다 녹아버림
                elif pan[nx][ny] == 1:
                    pan[nx][ny] = 0
                    visited[nx][ny] = 1
                    # 녹은 치즈의 갯수 count
                    count += 1

    # bfs가 한번 돌때마다
    # melt_cheese 배열에 녹은 치즈의 갯수가 추가될것
    melt_cheese.append(count)
    return count


N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
melt_cheese = []

time = 0
# 녹을 치즈가 더 없을때까지 반복
while True:
    # 녹은 시간 1 추가
    time += 1
    cnt = bfs()
    if cnt == 0:
        break

print(time-1)
# 맨 뒤에 값 출력하면 0임,
# 왜냐면 다 녹아도 한번은 bfs가 도니까
print(melt_cheese[-2])