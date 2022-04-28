
N = int(input())

# 이거 뭐 가운데집 아니야?
wich = sorted(list(map(int, input().split())))

# 정답입니다~

# 짝수일 경우에는 두 집이 후보군에 오르는데
# 두 집 중에 왼쪽(최솟값)이 선택되어야 하니까

if N % 2:
    print(wich[N//2])
else:
    print(wich[(N-1)//2])