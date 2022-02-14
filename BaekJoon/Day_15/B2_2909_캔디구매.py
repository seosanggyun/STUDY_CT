# 지폐의 액면가의 0의 갯수가 n이라면
# 지폐의 액면가는 10**n 임
# 사탕의 가격을 10**n으로 나눈 나머지가
# 액면가의 반보다 낮을경우 내림,
# 높을경우 올림

candy, bill = map(int,input().split())

# 사탕의 가격을 10**n으로 나눈 나머지
namergy = candy % (10**bill)

# 나머지가 액면가의 절반보다 낮을 경우
# 사탕 가격에서 나머지를 뺌 (내림)
if namergy < ((10**bill) // 2) :
    candy -= namergy
# 나머지가 액면가의 절반보다 높거나 같을경우
# 사탕 가격에 (액면가 - 나머지)를 더함 (올림)
# 예를 들어 182에 액면가 100원일 경우
# 182를 100으로 나눈 나머지는 82
# 100 - 82 + 182 = 200    
else:
    candy += (10**bill - namergy)

print(candy)