# 테스트 케이스의 개수 입력받음
T = int(input())

# 테스트 케이스의 개수 만큼 반복
for TC in range(T):

    #OX 문자열 입력받음
    OX = input()

    # 총점과 카운트 초기화
    # 카운트는 연속된 O의 갯수 셀거임
    score = 0
    count = 0

    # 입력받은 OX 문자열 반복문 돌려서
    for OXs in OX:
        # O를 찾으면 카운트 1씩 더하고
        # 그 카운트 값을 점수에 더함
        if OXs == 'O':
            count += 1
            score += count
        # 그러다가 X 만나면 카운트 0으로 초기화
        elif OXs == 'X':
            count = 0
    print(score)
    


