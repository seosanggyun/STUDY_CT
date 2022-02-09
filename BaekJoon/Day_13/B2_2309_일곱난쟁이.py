# 어떻게 풀거냐면..
# 리스트에서 9개의 요소들 중
# 2개의 요소를 빼고 다 더해서 100이 되면
# 그 상태의 리스트를 오름차순으로 정렬한 뒤
# 출력해줄거임

# deepcopy를 쓰기위해 copy import
import copy

# 난쟁이들의 키를 담을 리스트 초기화
heights_1 = []

# 난쟁이들의 키를 리스트에 입력받음
for h in range(9):
    heights_1 += [int(input())] 

# 리스트에서 9개의 요소들 중 i번째 요소를 빼고
# 남은 8개의 요소들 중 j번째 요소를 빼는
# 반복문을 돌릴건데
# deepcopy를 안해놓으면
# 리스트에서 모든 요소가 제거가 됨
# for문 시작 때 리스트 초기화를 위해 
# 원본을 다른 저장소에 저장해놓을 필요가 있다는 
# 느낌이 들어서 deepcopy 사용함

for i in range(9):
    # heights_2에 heights_1 넣어서 초기화
    heights_2 = copy.deepcopy(heights_1)
    # heights_2에서 i번째 요소 삭제
    del(heights_2[i])
    for j in range(8):
        # heights_3에 heights_2 넣어서 초기화
        heights_3 = copy.deepcopy(heights_2)
        # heights_3에서 j번째 요소 삭제
        del(heights_3[j])
        # 난쟁이들의 키 총합 초기화
        sum = 0
        # heights_3 리스트를 순회하여
        # 일곱 난쟁이들의 키 더해서 sum에 저장
        for k in heights_3:
            sum += k
        # 총합이 100일 때    
        if sum == 100:
            # 오름차순으로 정렬한 heights_3의 요소들을
            # 언패킹하고 줄바꿈으로 구분하여 출력
            # 언패킹 써보고 싶었음
            print(*sorted(heights_3), sep='\n')
            break
        # 이 까지만 하면 출력을 몇번 더하길래
    if sum == 100:
        # 바깥의 for문도 break 걸어줌    
        break


            
            