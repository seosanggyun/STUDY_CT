# 성냥이 박스에 들어가는지 알아내는 문제

# 각 변수들을 입력받아줌
N, W, H = map(int, input().split())

# 박스 안에서 가장 긴 구간은 대각선 구간
# 가로 세로 값을 입력받았으니 대각선 구함
P = (W**2 + H**2)**0.5

# N이 성냥의 개수이므로
# 성냥의 개수만큼 반복문을 돌면서
# 성냥의 길이를 입력받음
for a in range(N):
    length = int(input())
    # 성냥의 길이가 박스의 대각선길이보다 짧으면
    # 박스안에 들어감
    if length <= P:
        print('DA')
    else:
        print('NE')