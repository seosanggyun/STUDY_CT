from pprint import pprint

n = int(input())

tree = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n-1):
    a, b ,c = map(int, input().split())
    tree[a][b] = c
    tree[b][a] = c

    pprint(tree)
