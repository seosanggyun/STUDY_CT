# 테스트 케이스 개수 입력받음
T = int(input())

# 테스트 케이스 개수만큼 반복
for TC in range(T):

    # 정보 입력 받음
    Info = input().split()
    answer = ''
    # deleted = Info[1][Info[0]-1]
    print(Info[1].replace(Info[1][int(Info[0])-1], '',1))

    ### 쒸익..
    ### 이게 왜 문제가 있을까요 여러분
    
