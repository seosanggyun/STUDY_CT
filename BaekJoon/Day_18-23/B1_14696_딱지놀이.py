## 5분동안 쳐매기더니 30점 주네 써글놈이

N = int(input())
result = []
for tc in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_count_list = [0]*4
    B_count_list = [0]*4

    for i in range(4):
        A_count = A.count(i+1)
        A_count_list[i] = A_count
        B_count = B.count(i+1)
        B_count_list[i] = B_count

    if A_count_list[3] > B_count_list[3]:
        result.append('A')
    elif A_count_list[3] < B_count_list[3]:
        result.append('B')
    else:
        if A_count_list[2] > B_count_list[2]:
            result.append('A')
        elif A_count_list[2] < B_count_list[2]:
            result.append('B')
        else:
            if A_count_list[1] > B_count_list[1]:
                result.append('A')
            elif A_count_list[1] < B_count_list[1]:
                result.append('B')
            else:
                if A_count_list[0] > B_count_list[0]:
                    result.append('A')
                elif A_count_list[0] < B_count_list[0]:
                    result.append('B')
                else:
                    result.append('D')

print(*result)    