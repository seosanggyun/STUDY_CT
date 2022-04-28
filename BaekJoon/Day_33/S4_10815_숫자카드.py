import sys
input = sys.stdin.readline

N = int(input())
sg_card = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
test_card = list(map(int, sys.stdin.readline().rstrip().split()))


def ebun(test, sg_card, start, end):
    mid = (start+end) // 2
    # start가 end를 넘어섰다?
    # 결과가 없다~
    if start > end :
        ans.append(0)
    # mid번째 값과 일치한다?
    # 결과가 있다~
    elif test == sg_card[mid]:
        ans.append(1)
    # 비교하는 카드가 mid번째 값보다 크다?
    # mid + 1부터 end까지 다시 검색한다~
    elif test > sg_card[mid]:
        ebun(test, sg_card, mid+1, end)
    # 비교하는 카드가 mid번째 값보다 작다?
    # start 부터 mid -1 까지 다시 검색한다~
    elif test < sg_card[mid]:
        ebun(test, sg_card, start, mid-1)

ans = []
# 상근이 카드들 정렬 해줘야 이분탐색이 진행됨
# 왜?
sg_card.sort()

for i in test_card:
    start, end = 0, N-1
    ebun(i, sg_card, start, end)

print(*ans)