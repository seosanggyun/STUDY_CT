# 두 자연수 입력 받음
A, B = map(int, input().split())

# A와 B의 약수를 받을 리스트 초기화
a_list = []
b_list = []
# 공약수들을 받을 리스트 초기화
yak_list = []

# 1부터 A까지의 수 중 A의 약수 찾아서
# a_list에 저장
for a in range(1, A+1):
    if A % a == 0:
        a_list += [a]

# 1부터 B까지의 수 중 B의 약수 찾아서
# b_list에 저장
for b in range(1, B+1):
    if B % b == 0:
        b_list += [b]

# a_list와 b_list에 있는 숫자들을 비교해서
# 같은 숫자들만 yak_list에 저장
for a_yak in a_list:
    for b_yak in b_list:
        if a_yak == b_yak:
            yak_list += [b_yak]
            # yak에 최대 공약수 저장
            yak = max(yak_list)

# 최소 공배수는
# A를 최대공약수로 나눈 값에 B를 곱하면 나옴
# 경험적 추론
bae = ((A // yak) * B)



print(yak)
print(bae)


