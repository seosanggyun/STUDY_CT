# 갖고있는 병 + 오늘 얻은 병 // 교환 필요 병
# 이 마실 수 있는 음료 병수
# 그런데 또 마시고 나면 병이 생기니까
# 교환 하고 나면 생기는 병으로 또 교환하는 경우를
# 생각해야 함

e, f, c = map(int, input().split())

# bottels에 갖고있는 병 + 오늘 얻은 병 저장
bottles = e + f

# 결과값 초기화
result = 0

# 병 수가 교환 가능 병수보다 작아질 때 까지 반복
while bottles >= c:
    # 마실 수 있는 음료 병수를 result에 합산
    result += (bottles // c)
    # 병 수에 마실 수 있는 음료 병수와
    # 교환에 사용하지 못했던 병수를 더한 값을 저장
    bottles = (bottles // c) + (bottles % c)


print(result)