from pprint import pprint

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

gonggan = []
gonggan.append([1]*(w+3))
gonggan += [[1] + [0] * (w+1) + [1] for _ in range(h+1)]
gonggan.append([1]*(w+3))

if w - q - 1 <= 0:
    i = w - q - 1
else:
    i = (w - q - 1) % w

j = p + 1

# 꼭짓점 설정
gonggan[1][1] = 9
gonggan[1][w+1] = 9
gonggan[h+1][1] = 9
gonggan[h+1][w+1] = 9


flag = 1
count = 0

while count < t:
    # 1 우상향
    if flag == 1:
        if gonggan[i-1][j+1] == 0:
            i -= 1
            j += 1
            count += 1
    # 우상향 하다가 부딪히면
    # 좌상향이 됨
        elif gonggan[i-1][j+1] == 1:
            flag = 2
    # 우상향 하다가 꼭짓점을 만나면
    # 좌하향이 됨
        elif gonggan[i-1][j+1] == 9:
            i -= 1
            j += 1
            count += 1
            flag = 3

    # 2 좌상향
    elif flag == 2:
        if gonggan[i-1][j-1] == 0:
            i -= 1
            j -= 1
            count += 1
    # 좌상향 하다가 부딪히면
    # 좌하향이 됨
        elif gonggan[i-1][j-1] == 1:
            flag = 3     
    # 좌상향 하다가 꼭짓점을 만나면
    # 우하향이 됨
        elif gonggan[i-1][j-1] == 9:
            i -= 1
            j -= 1
            count += 1
            flag = 4
    
    # 3 좌하향
    elif flag == 3:
        if gonggan[i+1][j-1] == 0:
            i += 1
            j -= 1
            count += 1
        # 좌하향 하다가 부딪히면
        # 좌상향이 됨
        elif gonggan[i+1][j-1] == 1:
            flag = 2
        # 좌하향 하다가 꼭짓점을 만나면
        # 우상향이 됨    
        elif gonggan[i+1][j-1] == 9:
            i += 1
            j -= 1
            count += 1
            flag = 1   

    # 4 우하향
    elif flag == 4:
        if gonggan[i+1][j+1] == 0:
            i += 1
            j += 1
            count += 1
        # 우하향 하다가 부딪히면
        # 우상향이 됨
        elif gonggan[i+1][j+1] == 1:
            flag = 1
        # 우하향 하다가 꼭짓점을 만나면
        # 좌상향이 됨    
        elif gonggan[i+1][j+1] == 9:
            i += 1
            j += 1
            count += 1
            flag = 2    

print(j - 1, end=' ')
print(i - 3)


pprint(gonggan)