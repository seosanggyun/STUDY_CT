from pprint import pprint

count = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 다음 탐색지점을 찾는 함수
def daum(x,y):
    # 후보군을 저장할 배열
    candidate = []
    # 델타탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 만약 다음 지점이 도착지라면
        if nx == N - 1 and ny == N - 1:
            # 도착지에 대한 정보를 후보군에 저장하고
            candidate = [(arr[nx][ny], nx, ny)]
            # 도착지의 좌표를 바로 리턴
            return (candidate[0][1], candidate[0][2])
        
        # 만약 다음 지점이 도착지가 아니고
        # 범위를 벗어나지 않고
        # 방문한 적이 없으면
        elif 0 <= nx < N and 0 <= ny < N and visited[nx][ny] != 1:
            # 후보군에 추가
            candidate.append((arr[nx][ny],nx,ny))

    # 후보군의 0번째 값, 즉 루피가 작은 순서대로 정렬
    candidate.sort(key = lambda x: (x[0]))
    # 후보군의 0번째 좌표, 즉 루피가 가장 작은 지점의 좌표 리턴
    return (candidate[0][1], candidate[0][2])
'''
6
7 1 7 7 7 7
7 1 7 7 1 1
7 1 1 1 1 1
7 7 7 7 7 7
7 7 7 7 7 7
7 7 7 7 7 7

6
7 1 1 7 7 7
1 0 1 7 7 7
1 1 1 7 7 7
7 7 7 7 7 7
7 7 7 7 7 7
7 7 7 7 7 7
'''
# 결과값을 더해가면서 다음 탐색지점을 탐색하는 함수
def jelda(x, y):
    global result
    # 현재 좌표의 루피값을 결과값에 더하고
    result += arr[x][y]
    # 방문처리
    visited[x][y] = 1
    # 다음 좌표는 다음 함수로 설정
    nx, ny = daum(x, y)
    # 만약 다음 좌표가 도착지점이라면
    if nx == N-1 and ny == N-1:
        # 도착지점의 루피 값 결과에 더하고 리턴
        result += arr[N-1][N-1]
        return
    # 다음 좌표가 도착지점이 아니라면
    # 계속해서 탐색
    jelda(nx, ny)


while True:
    N = int(input())
    if N == 0:
        break
    else:
        result = 0
        count += 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range (N)]
    jelda(0,0)


    print(f'Problem {count}: {result}')
    # pprint(arr)
    # pprint(visited)

