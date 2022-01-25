
# R1과 S를 입력받음
R1, S = map(int, input().split())

# R2를 구하기 위해
# S = (R1 + R2)/2
# 에서 R2를 끄집어 냄
# 2S = R1 + R2
# 2S - R1 = R2
R2 = 2 * S - R1

print(R2)