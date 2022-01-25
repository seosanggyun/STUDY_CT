while True:
    input_E = input()

    if input_E == '#':
        break

    alphabet = input_E[0]
    sentence = input_E[1:].lower()

    count = sentence.count(alphabet)

    print('{} {}'.format(alphabet, count))
    