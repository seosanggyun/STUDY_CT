import copy

N, M = map(int, input().split())

card_1 = list(map(int, input().split()))
sum_1 = 0
sum_list = []

for i in range(N):
    card_2 = copy.deepcopy(card_1)
    sum_1 += card_2[i]
    sum_2 = copy.deepcopy(sum_1)
    del(card_2[i])
    for j in range(N-1):
        card_3 = copy.deepcopy(card_2)
        sum_2 += card_3[j]
        sum_3 = copy.deepcopy(sum_2)
        del(card_3[j])
        for k in range(N-2):
            sum_3 = sum_2
            card_4 = copy.deepcopy(card_3)
            sum_3 += card_4[k]
            sum_list += [sum_3]
    