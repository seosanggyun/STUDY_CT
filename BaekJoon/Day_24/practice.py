


def bfs(i, j):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    queue = []
    queue.append((start_i, start_j))

    while queue:
        i, j = queue.pop(0)

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < 16 and 0 <= nj < 16 and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                visited[ni][nj] = True
                queue.append((ni,nj))
    return


for tc in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[False]*16 for _ in range(16)]
    start_i, start_j = 0, 0
    end_i, end_j = 0, 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start_i = i
                start_j = j
            if arr[i][j] == 3:
                end_i = i
                end_j = j

    bfs(start_i, start_j)

    if visited[end_i][end_j] == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')




