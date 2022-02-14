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
    
N, M = map(int, input().split())

card = list(map(int, input().split()))
sum_list = []
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] > M:
                continue
            else:
                sum_list += [card[i] + card[j] + card[k]]
print(max(sum_list))