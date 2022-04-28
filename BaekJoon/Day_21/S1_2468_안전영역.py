N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


# print(arr)

area = []

count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i,j,water):
    global count
    # 델타 탐색 범위가 arr를 벗어나지 않도록 제한 둬야함
    if i < 0 or i >= N or j < 0 or j >= N:
        return False
    
    # arr의 지역이 water 초과일 경우
    # count에 + 1 해주고
    # 해당 지역을 -1로 바꿔줌 다시 탐색 안하게
    if arr[i][j] > water :
        count += 1
        arr[i][j] = -1
        for delta in range(len(dx)):
            dfs(i+dx[delta], j+dy[delta])
        return True

    # 이러면 arr를 탐색하다가 
    # water 초과인 지역을 발견하면
    # 해당지역 포함해서 
    # 주위에 water 초과인 높이로 연결되어있는
    # 지점이 모두 -1로 바뀌고
    # 지점의 수만큼 count 값이 증가해 있을 것임

    # 근데 이러면..
    # 딥카피를 꺼낼 수 밖에 없는데?
    # 이게 맞나?

    for k in range(N):
        for l in range(N):
            # arr의 지역을 하나하나 돌면서
            # dfs 함수를 돌려줌
            if dfs(k,l) == True:

                # True일 경우 area 리스트에
                # 카운트값을 저장
                area += [count]

                # 다음 단지의 집 수를 세기 위해
                # 카운트는 초기화 해줘야 함
                count = 0

print(len(area))
