# 숫자를 입력 받음
n = int(input())

# 규칙을 찾아야 함. 못 찾아서 구글링 함.
# 숫자를 8로 나누었을 때
# 나머지가 1 이면 엄지,
# 나머지가 2 or 0이면 검지,
# 나머지가 3 or 7이면 중지,
# 나머지가 4 or 6이면 소지,
# 나머지가 5 이면 약지
# 니까 엄지부터 순서대로 1, 2, 3, 4, 5 출력
finger = n % 8

if finger == 1:
    print(1)
elif finger == 2 or finger == 0:
    print(2)
elif finger == 3 or finger == 7:
    print(3)
elif finger == 4 or finger == 6:
    print(4)
else:
    print(5)