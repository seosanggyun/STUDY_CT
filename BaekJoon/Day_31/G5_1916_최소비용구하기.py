from heapq import heappop, heappush
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    Q = []
    # 시작 노드로 가기 위한 최단거리는 0,
    # 이 값을 큐에 삽입
    heappush(Q, (0,start))
    
    distance[start] = 0
    # 큐가 비어있지 않다면
    while Q:
        # 가장 짧은 거리 dist
        # 현재 노드 now
        dist, now = heappop(Q)
        
        if distance[now] != dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for node, cost in graph[now]:
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우
            if distance[node] > dist + cost:
                distance[node] = dist + cost
                # distance 배열의 현재 노드 값 갱신
                # 현재 cost와 현재 노드값을 heapq에 저장
                heappush(Q, (dist + cost, node))

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF for _ in range(N+1)]

for i in range(M):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b,cost))

start, end = map(int, sys.stdin.readline().rstrip().split())


dijkstra(start)

# 어째서?

print(distance[end])