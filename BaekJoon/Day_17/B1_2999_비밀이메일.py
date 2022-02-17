# 메세지를 입력받음
message = input()

# n에 메세지의 길이를 저장하고
n = len(message)
# n의 약수들을 저장하기 위한 리스트 초기화
n_list = []

# n의 약수들을 리스트에 저장
for a in range(1, n+1):
    if n % a == 0:
        n_list.append(a)

# n의 약수들의 개수가 홀수일 경우
if len(n_list) % 2:
    # n은 어떤 수의 제곱임
    # 예를 들어 n이 16일 경우
    # 약수는 1 2 4 8 16
    R, C = int(n**(1/2)), int(n**(1/2))
# n의 약수들의 개수가 짝수일 경우
else:
    # C에는 (약수들의 개수 / 2)와 같은 인덱스에 해당하는 약수가 들어가고
    # R에는 그 이전 인덱스의 약수가 들어가면 됨
    # 예를 들어 n이 6일 경우
    # 약수는 1 2 3 6
    R, C = n_list[int(len(n_list)*(1/2))-1], n_list[int(len(n_list)*(1/2))]

# 2차원 배열 선언
arr = [[0] * C for _ in range(R)]

# 메세지를 리스트로 변환
m_list = list(message)

# 메세지의 알파벳을 어떻게 2차원 배열에 하나하나 넣지?

# 카운트를 사용하면 된단다
count = 0

# 열 우선으로 문자열을 입력해야 하므로
# range(C) 먼저 돌고 그다음 range(R) 돌아야 함
for c in range(C):
    for r in range(R):
        arr[r][c] = m_list[count]
        # 한번 넣을때마다 카운트를 올려줘서
        # 해당 카운트에 해당하는 문자만 리스트에 저장되도록
        count += 1

# 행 우선으로 문자열을 출력해야 하므로
# range(R) 먼저 돌고 그다음 range(C) 돌아야 함    
for r in range(R):
    for c in range(C):
        print(arr[r][c], end='')
