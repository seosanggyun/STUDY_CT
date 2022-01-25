S = input()
K = input()

result = ''

for i in range(len(S)):
    T = ord(S[i]) - ord(K[i%len(K)])
    
    if S[i] == ' ':
        result += ' '

    
    elif T > 0:
        result += chr(T+96)

    else:
        result += chr(T+26+96)

print(result)