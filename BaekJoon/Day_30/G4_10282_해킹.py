import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    Q = []
    # 시작 노드로 가기 위한 최단거리는 0,
    # 이 값을 큐에 삽입
    heapq.heappush(Q, (0,start))
    
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

T = int(input())
for tc in range(1, T+1):
    n, d, c = map(int, input().split())
    start = c
    graph = [[] for _ in range(n+1)]
    distance = [INF for _ in range(n+1)]
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a,s))


    dijkstra(start)

    # 최댓값과 카운트 초기화
    max_dijk = 0
    count = 0

    # distance 배열 순회
    for i in distance:
        # 배열의 i 값이 INF가 아니고
        if i != INF:
            # 배열의 i 값이 max_dijk보다 클 때
            # max_dijk에 배열의 i 값 할당
            if max_dijk < i:
                max_dijk = i
            # 그리고 이건 컴퓨터가 한대 감염되었다는 뜻이므로
            # count +1
            count += 1
    print(count, max_dijk)


