C = int(input())

for a in range(C):
    N = list(map(int, input().split(' ')))

    total = 0
    count = 0

    for b in N[1:]:
        total += b
        avg = total / (len(N) - 1)

    for c in N[1:]:
        if c > avg:
            count += 1

    result = count / (len(N) - 1) * 100

    print('{:.3f}%'.format(result))
