n = int(input())

f1, f2 = map(int, input().split())

m = int(input())

relation = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())

    relation[x].append(y)
    relation[y].append(x)

# print(relation)

visited = [[-1] for _ in range(n+1)]

# print(visited)

def dfs(i):
    for r in relation[i]:
        if visited[r] == -1:
            pass
