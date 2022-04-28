
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 처음 값 초기화
left, right = 0, 0
tmp_sum = arr[0]
# 최댓값을 잡아줘야 하는데 이 길이는 수열의 길이인 N을 초과할 수 없음
min_length = N+1

while True:
    # 임시 합이 목표인 S보다 크거나 같으면
    # 왼쪽 포인터가 가리키는 수를
    # 임시 합에서 빼줌
    if tmp_sum >= S:
        tmp_sum -= arr[left]
        # 최소 길이 갱신
        min_length = min(min_length, right - left + 1)
        # 왼쪽 포인터 1 증가
        left += 1
    # 임시 합이 목표인 S보다 작으면
    # 오른쪽 포인터를 1 증가 시키고
    # 오른쪽 포인터가 N을 가리키면 갈때까지 간거니까 끝내주고
    # 그게 아니면 임시 합에 오른쪽 포인터가 가리키는 수를 더함
    else:
        right += 1
        if right == N:
            break
        tmp_sum += arr[right]

# S가 나오면 길이는 갱신이 되어 있을 것임
# 그니까 갱신이 안되어 있단 말은 S가 안나온다는거
if min_length == N+1:
    print(0)
else:
    print(min_length)


