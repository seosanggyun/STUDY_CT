

# word = list(input().split())

# def reverse_string(x):
#     x_list = list(x)
#     x_list = reversed(x_list)
#     x = ''.join(x_list)
#     return x

# print(word)


# gwal_idx = []

# for i in range(len(word)):
#     if word[i] == '<':
#         gwal_idx.append(i)
#     elif word[i] == '>':
#         gwal_idx.append(i)

# print(gwal_idx)

# word = reverse_string(word)
# print(word)
# print(''.join(word))




# 문자열을 리스트로 입력 받아줌
words = list(input())

# 결과값을 저장할 변수 result
result = ''

# <>가 나올 경우 그 부분은 뒤집으면 안되기 때문에
# <>의 내용을 따로 임시적으로 저장할 변수 tmp_word
tmp_word = ''

# <가 나오면 flag를 False로 바꾸고
# flag가 False인 동안에는 뒤집지 않고 tmp_word에 저장하며
# >가 나오면 flag를 True로 바꾸어 더이상 저장하지 않기 위해
# flag를 True로 초기화
flag = True


# 입력받은 문자열 순회
for i in words:
    # <가 등장한다면
    if i == '<':
        # flag를 False로 바꾸고
        flag = False
        # 이전까지 tmp_word에 저장되어 있던 값을 result에 저장
        result += tmp_word
        # 그리고 tmp_word에 < 저장
        tmp_word = i

    # >가 등장한다면
    elif i == '>':
        # flag를 True로 바꾸고
        flag = True
        # 이전까지 저장되어 있던 값에 >를 붙여서 result에 저장
        result += (tmp_word + '>')
        # tmp_word 비우기
        tmp_word = ''

    # 공백이 등장한다면
    elif i == ' ':
        # 공백 이전의 값들에 공백을 더해서 result에 저장
        result += tmp_word + i
        # tmp_word 비우기
        tmp_word = ''

    # flag가 True라면
    # 즉, <> 밖의 문자열이라면
    elif flag:
        # tmp_word에 순서를 뒤집어 저장
        tmp_word = i + tmp_word
    
    # 그 외의 경우
    else:
        # tmp_word에 한글자씩 저장
        tmp_word += i



# 로직이 끝난 뒤에 tmp_word에 값이 있으면 result에 저장

result += tmp_word
print(result)