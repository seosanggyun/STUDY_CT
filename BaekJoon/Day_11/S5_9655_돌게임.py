N = int(input())

if N % 2:
    print('SK')
else:
    print('CY')

# 진짜 얼탱이가 없다
# 빛의 서상균이 상근이가 되고
# 어둠의 서상균이 창영이가 되어
# 치열한 수싸움을 벌이면서
# 테스트케이스 5, 7, 9, 10, 12를 수기로 해본 결과
# 홀수일땐 무조건 상근이가 이기고
# 짝수일땐 무조건 창영이가 이기더라
# 뭔가 이거 재귀함수를 써야하나 싶긴 했는데
# 그냥 홀수 짝수로 돌려보니까
# 맞았대
# 채점 한 4분 돌리더라 백준도 당황한듯