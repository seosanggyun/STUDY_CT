N, M = map(int, input().split())

nlist = []
for i in range(1, N+1):
    nlist.append(i)

visited = [0 for _ in range(N+1)]

result = []

def dfs(depth):
    if depth == M:
        print(*result)
        return
    
    for i in range(N):
        # visited 배열의 i번째 요소가 0이라면
        if visited[i] == 0:
            
            # 결과 리스트에 i+1을 추가해주는데,
            # i가 0부터 시작하기 때문
            result.append(i+1)
            # print(*result)

            dfs(depth+1)

            # 방문표시
            # N과M(2) 에서는 방문표시를
            # 재귀가 돌기 전에 했었는데
            # 이번에는 재귀가 끝나고 해야 함
            # 왜냐면 비내림차순, 즉
            # 1 1, 2 2 와 같이 처음에 지정된 숫자도
            # 뒤에 추가가 되어야 하는데
            # 방문표시를 재귀 전에 해버리면
            # 같은 숫자는 추가가 안됨 
            visited[i] = 1

            # 돌아오면서 결과 리스트의 마지막 요소를 삭제
            result.pop()
            
            
            # 그리고 뒤 요소들을 방문하지 않은 것으로 설정하여
            # 중복되는 수열이 출력되지 않도록 함
            for j in range(i+1, N):
                visited[j] = 0
            # visited[i] = 0

dfs(0)