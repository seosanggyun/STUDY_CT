T = int(input())

for a in range(T):
    blank = input()
    N = int(input())
    total = 0

    for b in range(N):
        total += int(input())

    if total % N == 0:
        print('YES')
    else:
        print('NO')