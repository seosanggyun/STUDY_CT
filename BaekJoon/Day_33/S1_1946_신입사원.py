import sys
input = sys.stdin.readline

T = int(input())

for i in range(1, T+1):
    N = int(input())
    jiwonja = []
    count = 0
    for i in range(N):
        p_score, i_score = map(int, sys.stdin.readline().split())
        jiwonja.append((p_score, i_score))

    # 정렬하면 서류점수 순으로 정렬 됨
    jiwonja.sort()
    # print(jiwonja)
    # 일단 서류 1등은 무조건 합격이니까
    # 그사람의 면접점수가 곧 커트라인이 됨
    cutline = jiwonja[0][1]
    # 커트라인보다 낮아야 (등수니까) 합격임
    # 맨 처음 지원자
    # 합격했으니 카운트 1 더해주고
    count += 1
    # 나머지 지원자들 보면서
    for i in range(1, N):
        # 지원자의 면접점수 순위가
        # 커트라인보다 낮다
        # 순위가 낮다? 높다?
        if cutline > jiwonja[i][1]:
            # 합격
            # 카운트 1 더해주고
            count += 1
            # 커트라인은 이 합격자의 면접점수 순위가 됨
            cutline = jiwonja[i][1]

    print(count)

