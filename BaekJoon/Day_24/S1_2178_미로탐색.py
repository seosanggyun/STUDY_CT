from pprint import pprint

# print(maze)

# def DFS(x,y):
#     global cnt
#     visited[x][y] = 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < M and 0 <= ny < N and maze[nx][ny] == 1 and visited[nx][ny] == 0:
#             if maze[nx][ny] == -1:
#                 visited[nx][ny] = -1
#                 cnt += 1
#                 return cnt
#             if DFS(nx,ny):

def bfs(x, y):

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    Q = []
    Q.append((x, y))
    visited[x][y] = 1

    while Q:
        x, y = Q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and maze[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                Q.append((nx,ny))

    return visited[N - 1][M - 1]

N, M = map(int, (input().split()))

maze = [list(map(int, input())) for _ in range(N)] 
visited = [[0] * M for _ in range(N)]

print(bfs(0, 0))

pprint(visited)




