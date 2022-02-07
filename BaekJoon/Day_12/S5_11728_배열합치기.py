
# 배열 A와 B의 크기 입력
N, M = map(int, input().split())

# 배열 A와 B 입력
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 배열 B의 크기가 A보다 클 경우
# A의 요소들을 B에 추가하는게 더 이득
if M >= N:
    # 배열 A의 요소들을 B에 추가한 뒤
    for a in A:
        B.append(a)
    # 정렬
    B.sort()
    # 리스트의 숫자들을 문자열로 변환해야
    B = list(map(str, B))
    # join 쓸 수 있음
    result = ' '.join(B)

# 마찬가지로 배열 A의 크기가 B보다 클 경우
# B의 요소들을 A에 추가하는게 더 이득
else:
    # 배열 B의 요소들을 A에 추가한 뒤
    for b in B:
        A.append(b)
    # 정렬
    A.sort()
    # 리스트의 숫자들을 문자열로 변환해야
    A = list(map(str, A))
    # join 쓸 수 있음
    result = ' '.join(A)

print(result)
