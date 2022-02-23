## 5분동안 쳐매기더니 30점 주네 써글놈이

# N = int(input())

# for tc in range(N):
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))

#     A_count_list = []
#     B_count_list = []

#     for i in range(1, N+1):
#         A_count = A.count(i)
#         A_count_list.append(A_count)
#         B_count = B.count(i)
#         B_count_list.append(B_count)

#     if A_count_list[3] > B_count_list[3]:
#         print('A')
#     elif A_count_list[3] < B_count_list[3]:
#         print('B')
#     else:
#         if A_count_list[2] > B_count_list[2]:
#             print('A')
#         elif A_count_list[2] < B_count_list[2]:
#             print('B')
#         else:
#             if A_count_list[1] > B_count_list[1]:
#                 print('A')
#             elif A_count_list[1] < B_count_list[1]:
#                 print('B')
#             else:
#                 if A_count_list[0] > B_count_list[0]:
#                     print('A')
#                 elif A_count_list[0] < B_count_list[0]:
#                     print('B')
#                 else:
#                     print('D')

N = int(input())
result = []
for tc in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_count_list = [0]*4
    B_count_list = [0]*4

    for i in range(1, N+1):
        A_count = A.count(i)
        A_count_list[i-1] = A_count
        B_count = B.count(i)
        B_count_list[i-1] = B_count

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