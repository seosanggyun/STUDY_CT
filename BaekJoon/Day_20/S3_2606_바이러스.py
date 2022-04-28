import sys

sys.setrecursionlimit(10000)

#컴퓨터의 수
n = int(input())

# 연결된 컴퓨터 쌍의 수
c = int(input())

# 인접 리스트 graph로 입력 받음
graph = [[] for _ in range(n+1)]

# 연결된 컴퓨터 쌍의 수만큼 반복해주면서
# 리스트에 인접 컴퓨터 정보 입력
for i in range(c):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

# 방문한 컴퓨터 정보 저장
visited = [0] * (n + 1)

def dfs(graph, start, visited):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, start, visited)
    return True


dfs(graph, 1, visited)
print(sum(visited)-1)