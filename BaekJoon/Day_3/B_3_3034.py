N, W, H = map(int, input().split())

P = (W**2 + H**2)**0.5

for a in range(N):
    length = int(input())
    if length <= P:
        print('DA')
    else:
        print('NE')