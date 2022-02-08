### 0 0 0 나올때까지 무한반복
while True:
    # 삼각형의 세 변을 리스트로 받음
    Tri = list(map(int, input().split(' ')))
    
    # 0 0 0 나오면 반복 멈춰!
    if Tri[0] == Tri[1] == Tri[2] == 0:
        break
    
    # 직각삼각형의 조건
    # 빗변(가장긴변) 제곱 == 나머지 두 변 제곱의 합
    # 빗변 찾아서 저장
    Longest = max(Tri)
    # 삼각형 세 변 리스트에서 빗변 제거
    Tri.remove(Longest)
    
    # 빗변을 제외한 나머지 변 제곱들의 합과
    # 빗변의 제곱이 같을 경우 right 출력
    if Tri[0]**2 + Tri[1]**2 == Longest**2:
        print('right')
    
    else:
        print('wrong')


