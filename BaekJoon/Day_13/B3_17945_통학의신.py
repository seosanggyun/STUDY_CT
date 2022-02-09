# 문제 실컷 읽었더니..
# 나를 능멸해?

# A와 B값 입력
A, B = map(int, input().split())

# 판별식으로 뭐 할건 아닌데
# 자주 쓰이게 될 것 같아서 저장
d = (2*A)**2 - 4*B

# 결과값은 나중에 정렬해야 하므로
# 리스트로 받기위해 초기화
ans = []

# 두 근을 근의공식으로 구함
X = round((-(2*A) + d**(1/2)) / 2)
Y = round((-(2*A) - d**(1/2)) / 2)

# 두 근을 결과값에 추가 후 정렬
ans += [X, Y]
ans.sort()

# 중근일 경우 둘 중 하나만 출력
if X == Y:
    print(X)
# 그 외의 경우 둘 모두 출력
# 언패킹 써보고 싶었음    
else:
    print(*ans)