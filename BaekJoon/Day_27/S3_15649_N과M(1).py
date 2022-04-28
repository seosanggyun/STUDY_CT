
def perm(n, k):
    if n == k:
        print(*arr)
    else:
        for i in range(n, k):
            arr[i], arr[n] = arr[n], arr[i]
            perm(n+1, k)
            arr[i], arr[n] = arr[n], arr[i]


N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

perm(0, M)

