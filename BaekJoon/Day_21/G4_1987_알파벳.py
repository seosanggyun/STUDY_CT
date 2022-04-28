R, C = map(int, input().split())

arr = [list(map(str, input())) for _ in range(R)]

# print(arr)

# arr 지역을 좌측상단부터 시작해서 탐색하면서
# 해당 지역의 알파벳을
# visited_alpha에 저장해두고
# visited_alpha에 있는 알파벳은 방문하지 않는
# 로직을 짜보고자 함

visited_alpha = []

count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


