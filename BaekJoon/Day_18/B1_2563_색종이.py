# from pprint import pprint

T = int(input())
# 도화지를 100X100개의 0으로 구성된 배열로 초기화
dohwa = [[0]*100 for _ in range(100)]

# 색종이의 개수만큼 반복
for tc in range(T):
    # 색종이의 시작점 입력받음
    X, Y = map(int, input().split())
    # X가 색종이의 가로 시작점,
    # Y가 색종이의 세로 시작점임
    # 색종이는 크기가 10인 정사각형이므로
    # X에서 X+10, Y에서 Y+10까지의 범위를 돌면서
    # 도화지를 1로 색칠함
    for x in range(X, X+10):
        for y in range(Y, Y+10):
            dohwa[x][y] = 1
            
# 색종이만큼 다 색칠하고 난 뒤
# 넓이를 구해야 함
# 넓이는 1의 개수임
# 카운트 초기화            
count = 0
for i in range(100):
    for j in range(100):
        if dohwa[i][j] == 1:
            count += 1

print(count)

