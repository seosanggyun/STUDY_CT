from pprint import pprint

T = int(input())


def bfs(x,y):

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    Q = []
    Q.append((x,y))

    while Q:
        x, y = Q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and bat[nx][ny] == 1:
                bat[nx][ny] = 0
                Q.append([nx,ny])


for tc in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    bat = [[0] * M for _ in range(N)]
    for k in range(K):
        k1, k2 = map(int, input().split())
        bat[k2][k1] = 1
    for x in range(N):
        for y in range(M):
            if bat[x][y] == 1:
                bfs(x,y)
                bat[x][y] = 0
                cnt += 1

    print(cnt)

    # pprint(bat)




