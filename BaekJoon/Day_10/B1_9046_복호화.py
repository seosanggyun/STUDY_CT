# 테스트 케이스의 수 입력받음
T = int(input())

# 테스트 케이스의 수 만큼 반복
for TC in range(T):
    # 단어 입력받음
    word = input()
    # 최다 빈도 알파벳 초기화
    max_alpha = ''
    # 최다 빈도 알파벳 빈도 초기화
    max_count = 0

    # 알파벳 개수만큼 반복문 돌림
    for i in range(ord('a'), ord('z')+1):
        # 현재 카운트에 현재 단어의 알파벳 개수 저장
        cur_count = word.count(chr(i))
        
        # 만약 현재 카운트가 최다 빈도 카운트보다 크다면
        if cur_count > max_count:
            # 최다 빈도 알파벳에 해당 알파벳 저장
            max_alpha = chr(i)
            # 최다 빈도 카운트에 현재 카운트 저장
            max_count = cur_count

        # 만약 현재 카운트와 최다 빈도 카운트가 같다면    
        elif cur_count == max_count:
            # print('?')
            # 이렇게 하면 반복문 돌면서 물음표가 먼저 출력됨
            # 최다 빈도 알파벳에 물음표 저장
            max_alpha = '?'
        
    print(max_alpha)



    





    

