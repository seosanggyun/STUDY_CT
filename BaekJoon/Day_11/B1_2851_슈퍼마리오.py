# 버섯들의 점수를 받을 리스트 초기화
scores =[]

# 10개 버섯들의 점수를 입력받아 리스트에 저장
for A in range(10):
    N = int(input())
    scores += [N]

# 리스트에 있는 점수들을 하나하나 더해갈건데
# 총 점수가 100을 넘어서면 for문을 중단하고
# 이전의 총 점수와 비교하여 100과 더 가까운 값을 출력
# 
# 총 점수를 저장할 변수 초기화

total_score = 0

# 점수 리스트를 순회해서
for score in scores:
    # 이전 총 점수에 현재 총 점수 저장하고
    pre_total_score = total_score
    # 현재 총 점수에 리스트에 있는 버섯의 점수를 더함
    total_score += score

    # 만약에 총 점수가 100을 넘어서면
    if total_score > 100:
        # 또 만약에 이전 점수가 총 점수보다 100에 더 가깝다면
        if abs(pre_total_score - 100) < abs(total_score - 100):
            print(pre_total_score)
            break
        # 아니면 이전 점수보다 총 점수가 100에 더 가깝다면
        elif abs(pre_total_score - 100) > abs(total_score - 100):
            print(total_score)
            break
        # 아니면 이전 점수와 총 점수가 100에 똑같이 가깝다면
        else:
            # 총 점수 출력
            print(total_score)
            break
    # 만약에 총 점수가 딱뎀이라면
    elif total_score == 100:
        # 총 점수 출력
        print(total_score)
        break
# 만약에 버섯 다 더했는데 총 점수가 100 이하라면
# 총 점수 출력
if total_score < 100:    
    print(total_score)
    
