# import copy

# N, M = map(int, input().split())

# card_1 = list(map(int, input().split()))
# sum_1 = 0
# sum_list = []
# result_list = []

# for i in range(N):
#     card_2 = copy.deepcopy(card_1)
#     sum_1 += card_2[i]
#     sum_2 = copy.deepcopy(sum_1)
#     del(card_2[i])
#     for j in range(N-1):
#         card_3 = copy.deepcopy(card_2)
#         sum_2 += card_3[j]
#         sum_3 = copy.deepcopy(sum_2)
#         del(card_3[j])
#         for k in range(N-2):
#             sum_3 = sum_2
#             card_4 = copy.deepcopy(card_3)
#             sum_3 += card_4[k]
#             sum_list += [sum_3]
# for b in sum_list:
#     if b <= M:
#         result_list += [b]
# print(max(result_list))


# N장의 카드 중 3장의 합이 
# M을 넘지 않으면서 M에 최대한 가까워야함

# 카드의 개수 N과 딜러가 외칠 숫자 M 입력받음
N, M = map(int, input().split())

# 카드의 숫자들 입력받음
card = list(map(int, input().split()))

# 카드의 합들을 저장할 리스트 초기화
sum_list = []
# 결과값 초기화
result = 0
# 카드를 한장씩 뽑아서 총 세장 뽑아야 하니까
# for문을 세번 돌릴건데
# 시작 범위를 하나씩 좁혀 들어갈거임
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            # 카드 세장의 합이 M보다 클 경우 그냥 넘어감
            if card[i] + card[j] + card[k] > M:
                continue
            # 그 외의 경우, 즉
            # 카드 세장의 합이 M보다 작거나 같을 경우
            # 카드의 합들을 저장하는 리스트에 저장함
            else:
                sum_list += [card[i] + card[j] + card[k]]
# 리스트에서 최댓값 출력
print(max(sum_list))