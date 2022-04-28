N = int(input())

dohwa = [[0]*1001 for _ in range(1001)]

count = [0] * N
for tc in range(N):
    r, c, width, height = map(int, input().split())

    for rx in range(r, r + width):
        for cy in range(c, c + height):
            dohwa[rx][cy] = tc + 1
    
    for i in range(1001):
        for j in range(1001):
            if dohwa[i][j] == tc + 1:
                count[tc] += 1
                
print(count)
