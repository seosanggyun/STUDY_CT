N = int(input())
result = 0

def fact(n):
    if n > 1:
        result = n * fact(n-1)
    else:
        return 1
    
    return result
    

    

print(fact(N))
