from pprint import pprint

N, M, V = map(int, input().split())

def DFS(cur):
    visited_DFS[cur] = True
    print(cur, end=' ')
    # print(visited)

    for nxt in range(1, N+1):
        if G[cur][nxt] == 1 and visited_DFS[nxt] == False:
            DFS(nxt)


def BFS(cur):
    visited_BFS = [0]*(N+1)
    queue = []
    queue.append(cur)

    while queue:
        cur = queue.pop(0)
        if not visited_BFS[cur]:
            visited_BFS[cur] = True
            print(cur, end=' ')
            for nxt in range(1, N+1):
                if G[cur][nxt] == 1 and visited_BFS[nxt] == 0:
                    queue.append(nxt)


visited_DFS = [False for _ in range(N+1)]

# 인덱스 가지고 놀거니까
# 스택은 정점의 개수 + 1개로 해야함
# 0번 인덱스는 안쓸거니까

G = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1

# pprint(G)

DFS(V)
print()
BFS(V)



G = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1

visiteddfs = [0 for _ in range(N+1)]

def dfs(cur):
    visiteddfs[cur] = 1

    for nxt in range(1, N+1):
        if G[cur][nxt] == 1 and visiteddfs[nxt] == 0:
            dfs(nxt)

def bfs(cur):
    visitedbfs = [0 for _ in range(N+1)]
    Q = []
    Q.append(cur)

    while Q:
        cur = Q.pop(0)
        if visitedbfs[cur] == 0:
            visitedbfs[cur] == 1
            for nxt in range(1,N+1):
                if G[cur][nxt] == 1 and visitedbfs[nxt] == 0:
                    Q.append(nxt)