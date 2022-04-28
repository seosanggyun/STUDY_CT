import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    Q = []
    # 시작 노드로 가기 위한 최단거리는 0,
    # 이 값을 큐에 삽입
    heapq.heappush(Q, (0,start))
    distance = [INF for _ in range(N+1)]
    distance[start] = 0
    # 큐가 비어있지 않다면
    while Q:
        # 가장 짧은 거리 dist
        # 현재 노드 now
        dist, now = heapq.heappop(Q)
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            time = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우
            if time < distance[i[0]]:
                # distance 배열의 현재 노드 time 값 갱신
                distance[i[0]] = time
                # 현재 time과 현재 노드값을 heapq에 저장
                heapq.heappush(Q, (time,i[0]))
    return distance

N, M ,X = map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    a, b, time = map(int, input().split())
    graph[a].append((b,time))

result = 0

# 각각의 학생들이 파티장에서 집으로 가는 최단시간의 정보가 담긴
# coming_home
coming_home = dijkstra(X)
# print(coming_home)

for i in range(1, N + 1):
    # 각각의 학생들이 파티장에 가는 최단시간의 정보가 담긴
    # going_party
    going_party = dijkstra(i) 
    # print(going_party)

    # 결과값은 i기준에서 파티장에 가는 시간 + 파티장에서 i(집)으로 가는 시간이 가장 큰 값
    result = max(result, going_party[X] + coming_home[i])

print(result)

    
