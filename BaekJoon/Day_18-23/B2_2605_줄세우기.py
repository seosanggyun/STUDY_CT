# 뭐야 이거 뒤집으면 되네?

# 학생들이 뽑은 번호의 위치에
# 학생들을 insert 하고
# 그 리스트를 역순으로 출력하면
# 정답이 나옴

n = int(input())
# 학생들이 뽑은 번호 리스트
bbob = list(map(int, input().split()))
# 학생들 순서 리스트
students = []
for i in range(n):
    # insert(a,b) 는
    # a의 위치에 b를 넣는 함수임
    # 즉 학생들이 뽑은 번호(위치)에
    # 학생들을 할당

    # i는 0부터 시작하는데
    # 학생은 1부터 시작하니까
    # i+1이 학생임
    students.insert(bbob[i],i+1)

# 역순으로 저장
students.reverse()
# 언패킹으로 출력
print(*students)

