# import sys;
# from pprint import pprint
#
# sys.stdin = open('algo2_sample_in.txt')

T = int(input())


def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    global result
    life = 2
    count = 0
    visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    Q = []
    Q.append((x, y))

    while Q:
        cur = Q.pop(0)
        i, j = cur[0], cur[1]
        if arr[i][j] == 3:
            result = count
            return

        if arr[i][j] == 1 and life != 0:
            arr[i][j] = 0
            life -= 1

        if visited[i][j] == 0:
            visited[i][j] = 1
            count += 1
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    Q.append((nx, ny))


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    result = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i
                sj = j
            if arr[i][j] == 3:
                ei = i
                ej = j
    bfs(si, sj)

    print(f'{tc} {result}')
    # pprint(arr)