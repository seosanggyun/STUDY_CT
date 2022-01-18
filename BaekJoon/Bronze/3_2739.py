# N을 입력 받은 뒤,
N = int(input())

# 구구단을 출력해야 하니까
# for 반복문으로 1부터 9까지 반복할 수 있게 range(1,10) 설정
for i in range(1,10):
    # 'N * i = N*i' 라고 출력되어야 하므로
    # 문자열 포매팅을 사용해
    # N과 i 포매팅, N*i를 포매팅 후 출력
    print('{} * {} = '.format(N, i) + '{}'.format(N * i))
