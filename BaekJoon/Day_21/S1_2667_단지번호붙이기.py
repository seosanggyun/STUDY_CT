N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

# 어떻게 적용시켜야 하지??
# 방문했다는 기록을 어떻게 남겨야 하지??

danji = []

count = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 어떤 함수를 만드냐면
# 방문한 곳이 1인 경우,
# 해당 지역을 0으로 바꾸고
# 델타 탐색으로 상하좌우를 보면서
# 1을 찾을 거임
# 그럴때마다 count + 1

def dfs(i,j):
    global count
    # 델타 탐색 범위가 arr를 벗어나지 않도록 제한 둬야함
    if i < 0 or i >= N or j < 0 or j >= N or arr[i][j] == 0:
        return False
    
    # arr의 지역이 1일 경우
    # count에 + 1 해주고
    # 해당 지역을 0으로 바꿔줌 다시 탐색 안하게
    # if arr[i][j] == 0:
    count += 1
    arr[i][j] = 0
    for delta in range(len(dx)):
        dfs(i+dx[delta], j+dy[delta])
    return True
    

    # 이러면 arr를 탐색하다가 1을 발견하면
    # 해당지역 포함해서 
    # 주위에 1로 연결되어있는
    # 한 단지가 모두 0으로 바뀌고
    # 단지의 수만큼 count 값이 증가해 있을 것임


for k in range(N):
    for l in range(N):
        # arr의 지역을 하나하나 돌면서
        # dfs 함수를 돌려줌
        if dfs(k,l) == True:

            # True일 경우 danji 리스트에
            # 카운트값을 저장
            danji += [count]

            # 다음 단지의 집 수를 세기 위해
            # 카운트는 초기화 해줘야 함
            count = 0

print(len(danji))
danji = sorted(danji)
for h in danji:
    print(h)

    
