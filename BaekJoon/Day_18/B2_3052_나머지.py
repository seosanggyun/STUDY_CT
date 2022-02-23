
# 10개의 숫자들을 42로 나눈 나머지를 구하고
# 서로 다른 값이 몇 개 있는지 출력

# 10개의 숫자들을 리스트로 입력받음
arr = [int(input()) for _ in range(10)]

# 나머지들을 저장할 리스트 초기화
namergy_list = []

# arr에 있는 숫자들을 42로 나눈 나머지를
# 나머지 리스트에 더해줌
for i in arr:
    namergy_list.append(i % 42)

# 모든 숫자가 같더라도
# 서로 다른 나머지의 숫자는 1이므로
# count를 1로 초기화
count = 1

# 나머지 리스트를 정렬해줌
namergy_list.sort()

# 앞에서부터 연속된 두개의 요소만 비교해서
# 값이 다를 경우 카운트 1 증가
# 정렬을 해놓았으므로 연속된 두개의 요소만 비교해도 됨
for j in range(10 - 1):
    if namergy_list[j] != namergy_list[j+1]:
        count += 1

print(count)

