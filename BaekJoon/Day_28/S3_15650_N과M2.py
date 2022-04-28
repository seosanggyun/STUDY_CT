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
            # 방문표시
            visited[i] = 1
            
            # 결과 리스트에 i+1을 추가해주는데,
            # i가 0부터 시작하기 때문
            result.append(i+1)
            # print(*result)

            dfs(depth+1)

            # 돌아오면서 결과 리스트의 마지막 요소를 삭제
            result.pop()
            
            # 그리고 뒤 요소들을 방문하지 않은 것으로 설정하여
            # 중복되는 수열이 출력되지 않도록 함
            # for j in range(i+1, N):
            #     visited[j] = 0
            visited[i] = 0
dfs(0)





