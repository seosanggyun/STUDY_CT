import sys
input = sys.stdin.readline

N = int(input())
p = [0] * (N + 1)
for i in range(N + 1):
    p[i] = i


def findset(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[findset(y)] = findset(x)


def find_bridge():
    for i in range(2, N+1):
        if island != findset(i):
            print(island, i)
            return

# 입력값 받아서 다리 연결해줌
for _ in range(N-2):
    x, y = map(int, input().split())
    union(x,y)

island = findset(1)
find_bridge()


