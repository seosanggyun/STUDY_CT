# 카드의 개수 입력받음
N = int(input())
# 카드의 번호를 입력받을 리스트 초기화
card = []

# 카드는 1부터 N까지의 번호가 붙어있으니까
# N의 개수만큼 반복문 돌면서
# card 리스트에 N+1을 저장해줌
for A in range(N):
    card += [A+1]

# N-1번의 순회를 돌면서
for B in range(N-1):
    # 제일 위에 있는 카드의 번호를 먼저 출력하고
    print(card[0], end=' ')
    # 제일 위에 있는 카드 제거
    del(card[0])
    # 그 뒤 제일 위에 있는 카드를 맨 밑으로 옮김
    card.append(card[0])
    del(card[0])
    # 반복
# 맨 마지막에 남은 카드번호 출력
print(card[0])
