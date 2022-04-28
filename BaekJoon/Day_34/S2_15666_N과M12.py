N, M = map(int, input().split())

nlist = sorted(list(map(int, input().split())))

result = []

def dfs(start):
    # result 배열에 결과값을 저장할 건데
    # 그 결과 값의 길이가 M일 경우 출력
    if len(result) == M:
        print(*result)
        return

    # 중복을 피하기 위한 remember 변수
    # 0으로 초기화, 입력으로 주어지는 수는 자연수 이기 때문
    remeber = 0

    # start부터 N까지 반복하면서
    # nlist 에 있는 숫자들을 볼 것임
    for i in range(start, N):
        
        # 주어진 입력을 정렬 했기 때문에
        # 다음으로 마주치는 숫자가
        # 같으면 곧 중복수열이기 때문에 
        # 같지 않은 숫자를 result에 저장함
        if remeber != nlist[i]:
            result.append(nlist[i])
            # 저장했으면 remember도 현재 숫자로 바꿔줌
            remeber = nlist[i]
            dfs(i)
            result.pop()
        

dfs(0)