I = list(map(int, (input().split())))

max = 0

for a in I:
    
    if a >= max:
        max = a
    
I.remove(max)

s_max = 0

for b in I:

    if b >= s_max:
        s_max = b

print(s_max)