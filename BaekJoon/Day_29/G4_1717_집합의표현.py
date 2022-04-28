import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = [0] * (n + 1)
for i in range(n + 1):
    p[i] = i


# print(p)

def findset(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[findset(y)] = findset(x)
    # x = findset(x)
    # y = findset(y)
    #
    # if x != y:
    #     p[y] = x

    # 시간초과 범인은 input 이었다


for _ in range(m):
    calc_type, a, b = map(int, input().split())

    # 0일때 합집합
    if calc_type == 0:
        union(a,b)

    # 1일때 같은 집합인지 확인
    elif calc_type == 1:
        if findset(a) == findset(b):
            print('YES')
        else:
            print('NO')

