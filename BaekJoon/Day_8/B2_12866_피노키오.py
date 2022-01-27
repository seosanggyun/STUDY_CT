# 염..색체..
import itertools

L = int(input())
S = list(input())

# 같은 염기더라도 염기열의 어디에 위치해있는지에 따라서
# 달라진다?

result = list(map(''.join, itertools.permutations(S)))
print(result)

## ???