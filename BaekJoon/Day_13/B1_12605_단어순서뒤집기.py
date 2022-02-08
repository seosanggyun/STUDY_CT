
# 테스트케이스의 개수 입력
N = int(input())

# Case # 뒤에 들어갈 숫자인 카운트 초기화
count = 0

# 테스트케이스의 개수만큼 반복
for tc in range(N):
    # 단어 입력 받음
    words = input()
    # 카운트 +1
    count += 1
    
    # 입력받은 단어를 띄어쓰기로 구분하여 리스트에 저장
    word_list = words.split()
    # 리스트 역순으로 바꿈
    word_list.reverse()
    # 바뀐 리스트를 요소사이에 공백을 추가하여 
    # 문자열로 바꾼 뒤 저장
    word_result = ' '.join(word_list)

    # 출력
    print(f'Case #{count}: {word_result}')