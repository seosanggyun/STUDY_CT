# 일과 월 입력
D, M = map(int, (input().split()))

# 어떻게 할거냐면
# 월을 일 단위로 바꿔서
# 입력받은 D에 더한 뒤
# 7로 나눠서 그 나머지에 해당하는 값으로
# 요일을 찾을거임

# 2009년은 윤년이 아니므로 2월은 28일까지 있음
# 매달의 일 수를 리스트로 저장
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 2009년 1월1일부터 1주일간의 요일을 리스트로 저장
first_of_2009 = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']

# 총 일수 초기화
days = 0

# 만약에 2월 13일의 요일을 찾고싶으면
# 1월의 일수와 13을 더한 수가 총 일수임
# 따라서 for문 range범위는 M-1
for a in range(M-1):
    # 총 일수에 M월까지의 일수 더함
    days += month_day[a]
# 총 일수에 D일수 더함
days += D

# 총 일수를 7로 나눈 나머지 저장
Cycle = days % 7

print(first_of_2009[Cycle - 1])