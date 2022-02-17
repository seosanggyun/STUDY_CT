N, M = map(int, input().split())
A = list(map(int, input().split()))

bit = [0]*N
count = 0

# 모든 경우의 수 중, 공집합 제외
for i in range(1 << N):
    result = 0
        # j는 arr의 idx 이므로 0부터 조회하여야
        # 모든 요소 포함여부 확인 가능
    for j in range(N):
        if i & (1 << j):
            print(A[j], end=' ')
            result += A[j]
    if result == M:
        count += 1   

print(count)
    

    