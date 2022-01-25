# 세 정수를 받아 두번째로 큰 정수를 출력

# 세 정수를 리스트로 받음
I = list(map(int, (input().split())))

# 최댓값 초기화
max = 0
# 리스트로 받은 세 정수를 순회하여 최댓값 찾기
for a in I:
    
    if a >= max:
        max = a
    # 최댓값을 찾은 후 최댓값을 리스트에서 제거
I.remove(max)

# 최댓값을 제거했으니 자연스럽게 리스트에 남은
# 값들 중 최댓값이 두번째로 큰 정수
s_max = 0

for b in I:

    if b >= s_max:
        s_max = b

print(s_max)