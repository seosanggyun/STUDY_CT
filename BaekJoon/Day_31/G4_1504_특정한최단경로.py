from heapq import heappop, heappush
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    Q = []
    distance = [INF for _ in range(N+1)]
    # 시작 노드로 가기 위한 최단거리는 0,
    # 이 값을 큐에 삽입
    heappush(Q, (0,start))
    distance[start] = 0
    # 큐가 비어있지 않다면
    while Q:
        # 가장 짧은 거리 dist
        # 현재 노드 now
        dist, now = heappop(Q)
        # 현재 노드와 연결된 다른 인접 노드 확인
        for node, cost in graph[now]:
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우
            if distance[node] > dist + cost:
                distance[node] = dist + cost
                # distance 배열의 현재 노드 값 갱신
                # 현재 cost와 현재 노드값을 heapq에 저장
                heappush(Q, (dist + cost, node))
    return distance

N, E = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    # 무방향 그래프라고 했으니까
    # 두 정점에 같은 cost 각각 넣어줌
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, sys.stdin.readline().rstrip().split())


# 1 - v1 - v2 - N
# 1 - v2 - v1 - N

# 1번에서 다른 모든 노드로 가는 다익스트라
# 1번 ~ v1 비용 찾는 용도
dp1 = dijkstra(1)

# v1에서 다른 모든 노드로 가는 다익스트라
# v1 ~ v2 비용 찾는 용도
dp2 = dijkstra(v1)

# v2에서 다른 모든 노드로 가는 다익스트라
# v2 ~ N 비용 찾는 용도
dp3 = dijkstra(v2)

result = min(dp1[v1] + dp2[v2] + dp3[N], 
            dp1[v2] + dp3[v1] + dp2[N])

if result >= INF :
    print(-1)
else:
    print(result)


