import sys

sys.setrecursionlimit(10000)

# 정점의 개수 N
# 간선의 개수 M
N, M = map(int, input().split())

# 인접 리스트 graph로 입력 받음
graph = [[]*N for _ in range(N+1)]

# 연결된 간선의 수만큼 반복
# 그래프 채워 나감
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 정보 저장
visited = [0] * (N + 1)

# print(graph)

count = 0


def dfs(graph, start, visited):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, start, visited)

for j in range(1, len(visited)):
    if visited[j] == 0:
        count += 1
        dfs(graph, i, visited)
            
print(count)