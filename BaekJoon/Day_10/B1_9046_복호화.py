T = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
beta = 'wghuvijxpqrstacdebfklmnoyz'
alpha = list(alpha)
beta = list(beta)
code = ''
for TC in range(T):
    word = input()
    word = list(word)
    for c in word:
        if c == ' ':
            code += ' '
        else :
            code += beta[alpha.index(c)]
    # word = ''.join(word)
    code = list(code)
    max_count = 0
    for freq in code:
        if code.count(freq) > max_count:
            max_count = code.count(freq)
            manytime = freq
        elif code.count(freq) == max_count:
            manytime = '?'
    print(manytime)
    





    

