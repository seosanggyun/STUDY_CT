# 테스트 케이스의 수 입력받음
T = int(input())

# 테스트 케이스의 수 만큼 반복
for TC in range(T):
    # H = 층수, W = 방의 수, N = 번째 손님
    H, W, N = map(int, input().split())

    # 어떻게 풀거냐면
    # 어차피 순서 101 201 301 401 이런식으로 갈거니까
    # 각 층의 1호 라인 먼저 나열되어 있고
    # 각 층의 2호 라인이 그다음에 나열되어 있는 식의
    # 리스트를 만들어서
    # 그 리스트 순서대로 방 배정해줄거임 토달지마셈

    # 방 리스트 초기화
    room_list = []

    # 1호라인 먼저 리스트에 넣어야 하니까
    # 호텔 가로넓이 먼저 순회 돌림
    for w in range(W):
        # 방 이름은 리스트에 넣을 때 마다 초기화 되어야 하니까
        # for 문 시작할 때 문자열로 초기화
        room = ''
        # room_h + room_w 의 형식으로 방이름 만들거임
        # room_w에 순회돌린 값 + 1 할당해줌
        # range로 돌리면 0호부터 돌아가니까
        room_w = str(w+1)

        # 7호 같은경우는 07호로 저장될 수 있게
        if len(room_w) == 1:
            room_w = '0' + room_w
        # room에 더해서 저장해줌
        room += room_w
        # 그다음 층수 반복문 돌려서 순회해줌
        for h in range(H):
            # room에 호수 초기화
            # room = room_w
            # room_h에 순회돌린 값 + 1 할당해줌
            # range로 돌리면 0층부터 돌아가니까
            room_h = str(h+1)
            # 방이름에 층수 + 호수 저장
            room = room_h + room_w
            # 방이름을 방이름 리스트에 더하기
            room_list += [room]  
    # 방이름 리스트에서 N-1번째 인덱스의 방이름이
    # N번째 손님이 묵을 방
    print(room_list[N-1])
        
# 와씨 풀었따