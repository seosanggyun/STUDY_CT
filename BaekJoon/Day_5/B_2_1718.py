S = input()
K = input()

result = ''

for i in range(len(S)):
    if S[i] == ' ':
        result += ' '
    else:
        result += (ord(S[i]) - ord(K[i]))