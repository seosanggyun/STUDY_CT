
# 단어 입력 받아줌
word = input()

# 크로아티아 알파벳을 리스트에 저장
kro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 단어에 있는 크로아티아 알파벳을
# 크로아티아 알파벳 리스트를 참조하여
# 전부 문자열 1로 바꾸어줌
for i in kro_alpha:
    word = word.replace(i, '1')

# 알파벳의 개수를 알아낸다는게
# 결국에는 문자열의 길이를 알아내는 거랑 같음
print(len(word))      

# 이게 되네?