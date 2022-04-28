N, M = map(int, input().split())
A = list(map(int, input().split()))

bit = [0]*N
count = 0

for i in range(1 << N):
    result = 0
        
    for j in range(N):
        if i & (1 << j):
            print(A[j], end=' ')
            result += A[j]

    if result == M:
        count += 1   

print(count)
    
# 땡
    