T = int(input())

# 정정당당하게 풀었다

for a in range(T):
    M = input()
    M_list = M.split()
    if M_list[1] == '+' and (int(M_list[0]) + int(M_list[2])) == int(M_list[4]):
        print('correct')
    elif M_list[1] == '*' and (int(M_list[0]) * int(M_list[2])) == int(M_list[4]):
        print('correct')
    elif M_list[1] == '-' and (int(M_list[0]) - int(M_list[2])) == int(M_list[4]):
        print('correct')
    elif M_list[1] == '/' and (int(M_list[0]) / int(M_list[2])) == int(M_list[4]):
        print('correct')
    else:
        print('wrong answer')
