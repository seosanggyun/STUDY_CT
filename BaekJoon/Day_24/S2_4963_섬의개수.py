from pprint import pprint


def bfs(x,y):

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    
    Q = []
    Q.append((x,y))

    global count
    count += 1
    while Q:
        x, y = Q.pop(0)
        jido[x][y] = 0

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and jido[nx][ny] == 1:
                jido[nx][ny] = 0
                Q.append((nx,ny))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    jido = [list(map(int, input().split())) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if jido[i][j] == 1:
                bfs(i,j)
    # pprint(jido)

    print(count)


