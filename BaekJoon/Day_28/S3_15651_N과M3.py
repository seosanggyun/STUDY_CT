N, M = map(int, input().split())

nlist = []
for i in range(1, N+1):
    nlist.append(i)

# visited = [0 for _ in range(N+1)]

result = []

def dfs(depth):
    if depth == M:
        print(*result)
        return
    
    # 중복을 고려할 필요가 없으니
    # 방문처리를 해주지 않으면
    # 모든 경우의 수에 대해 재귀 계속 실행됨

    for i in range(N):
        result.append(i+1)
        dfs(depth+1)
        result.pop()

dfs(0)