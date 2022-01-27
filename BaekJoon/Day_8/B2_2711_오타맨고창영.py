# 테스트 케이스 개수 입력받음
T = int(input())

# 테스트 케이스 개수만큼 반복
for TC in range(T):

    # 정보 입력 받음
    Info = input().split(' ')
    # 오타를 낸 위치를 정수로 저장
    order = int(Info[0])

    # 문자열을 리스트로 저장
    # 왜 리스트로 저장하냐면
    # 문자열로 해봤다가 피봤음
    # 리스트로 하면 요소 변경이 쉬워
    spells = list(Info[1])

    # 스펠링 리스트에서 오타가 난 위치(order-1)의
    # 스펠링을 제거함
    del(spells[order-1])

    # 리스트 형태의 spells를 문자열로 변환하여
    # answer에 저장
    answer = ''.join(spells)
    print(answer)

    
