N, M = map(int, input().split())

count = 1

def bfs(cur):

    visited = [0 for _ in range(N+1)]
    Q = []
    Q.append(cur)
    count = 1

    while Q:
        cur = Q.pop(0)
        if not visited[cur]:
            visited[cur] = 1
            for nxt in range(1, N+1):
                if comters[cur][nxt] == 1 and visited[nxt] == 0:
                    Q.append(nxt)
                    count += 1
                    
    return count


comters = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    # comters[a][b] = 1
    comters[b][a] = 1

results = []
max_count = 0

for i in range(1, N+1):
    count = bfs(i)
    if max_count < count:
        max_count = count
        results.append(i)

print(results)

