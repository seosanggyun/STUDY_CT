
# 리스트로 몸무게와 키를 입력받아서
# 리스트의 각 요소를 비교하여 등수를 출력하려고 했는데
# 몸무게와 키 둘 다 
# 비교대상보다 클 때 등수가 높음 (숫자는 작아짐)
# 이 부분 어떻게 코드로 표현해야 할지 감이 안 와서 구글링

# 2중 for문으로 i와 j항목을 모두 순회하면서
# i번째 항목의 몸무게와 키가
# j번째 항목의 몸무게와 키보다 작을 경우
# 1로 초기화 되어 있던 rank에
# 1씩 더해주면 그대로 등수가 됨



n = int(input())

dungchi_list = []

for a in range(n):
    dungchi_list += [list(map(int, input().split()))]

# 덩치 리스트를 두 번 순회 하면서
for i in dungchi_list:
    # i 번째 항목의 등수를 출력해야 하므로
    # 두번째 for문 돌기 전에 rank를 1로 초기화
    rank = 1
    # 두번째 for문 순회
    for j in dungchi_list:
        # i번째 항목의 몸무게와 키 모두
        # j번째 항목의 몸무게와 키보다
        # 작을 경우 등수 +1
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')

