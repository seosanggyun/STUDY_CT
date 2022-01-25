# 각 피스별로 다르게 변수 선언, 값 입력 받기
K, Q, R, V, KN, P = map(int, input().split())

# 올바른 세트의 피스 개수 저장
k = 1
q = 1
r = 2
v = 2
kn = 2
p = 8

# 올바른 세트의 피스 개수 - 입력받은 값이 곧 필요한 피스의 개수 (음수라면 제거)
print(k - K, end=' ')
print(q - Q, end=' ')
print(r - R, end=' ')
print(v - V, end=' ')
print(kn - KN, end=' ')
print(p - P, end=' ')