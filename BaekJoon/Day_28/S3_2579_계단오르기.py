from collections import deque

N = int(input())
stairs = []
for _ in range(N):
    stair = int(input())
    stairs.append(stair)

dx = [1, 2]
result = 0
tmp = 0

def score(x):
    global result
    tmp = 0
    Q = deque()
    Q.append(x)

    while Q:
        cur = Q.popleft()
        
        if cur == N:
            if tmp > result:
                result = tmp
            return

        tmp += stairs[cur]

        for i in range(2):
            nx = x + dx[i]

            if nx < N:
                Q.append(nx)
                
# print(stairs)

score(0)
print(result)
