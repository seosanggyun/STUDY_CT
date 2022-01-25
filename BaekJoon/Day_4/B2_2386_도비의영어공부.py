# 영어 문장과 알파벳이 주어지면 그 알파벳이 문장에서 몇 번 나타나는지

# 반복문 돌려서 알파벳과 문장을 문자열 형태로 입력받음
# 무한으로 즐겨요
while True:
    input_E = input()
    # '#'을 만나면 입력 그만 받음
    if input_E == '#':
        break
    # 알파벳은 문자열의 맨 앞에 있음
    alphabet = input_E[0]
    # 문장은 그외의 모든 문자열이며 
    # 알파벳의 유무만 판단하면 되니까 소문자로 다 바꿔줌
    sentence = input_E[1:].lower()
    # 알파벳과 문장의 일치하는 부분을 count()메서드로 셈
    count = sentence.count(alphabet)

    print('{} {}'.format(alphabet, count))
    