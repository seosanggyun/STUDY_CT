import sys

input = sys.stdin.readline
from pprint import pprint
from collections import deque

# 무게를 함수에 집어 넣었을 때,
# 이 무게를 가지고 factory_a에서 factory_b까지 도달할 수 있는지
# 여부를 판단하기 위한 bfs
# 결과값은 visited[factory_b]로 반환하여
# 1일 경우 도착 가능, 0일 경우 도착 불가

def bfs(weight):
    visited = [0 for _ in range(N + 1)]
    Q = deque()
    Q.append(factory_a)
    visited[factory_a] = 1
    while Q:
        cur = Q.popleft()
        for nxt, w in data[cur]:
            if visited[nxt] == 0 and w >= weight:
                visited[nxt] = 1
                Q.append(nxt)
    return visited[factory_b]


N, M = map(int, input().split())
data = [[] for _ in range(N + 1)]

start = 1000000000
end = 1

for _ in range(M):
    A, B, C = map(int, input().split())
    data[A].append((B, C))
    data[B].append((A, C))

    # start 값에 C와 비교해서 작은 값을 넣고,
    # end 값에 C와 비교해서 큰 값을 넣음
    # 전체 지도에서 가장 무거운 중량제한이 end에,
    # 가장 가벼운 중량제한이 start에 입력됨
    start = min(start,C)
    end = max(end,C)

factory_a, factory_b = map(int, input().split())

# 가장 무거운 중량제한을 찾으면 되므로
# 이분탐색을 하면서 중량을 찾아나설 것
# 결과에 가장 가벼운 값인 start를 넣어주고
# 공장에 도착할 수 있을 동안
# start + 1씩, end에 - 1씩 해주면서
# 최대 무게를 찾음
result = start

while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
