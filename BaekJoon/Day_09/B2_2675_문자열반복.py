## 테스트 케이스의 개수 입력받음
T = int(input())
## 반복횟수 R과 문자열 S를 문자열로 입력받음
R, S = input().split()
## 반복횟수 R을 정수로 형변환 후 저장
R = int(R)

# 테스트 케이스의 개수만큼 반복
for TC in range(T):
    # 문자열 안에 있는 글자들 순회
    for letters in S:
        # 문자열 안의 글자들을 
        # 문자열이 R번 반복된 문자열로
        # 교체해줌
        S = S.replace(letters,letters*R)

print(S)

## 메모리를 사 이 ㅆ
        
