
# Sentence = input()
# Person = 'sweet'
# if Person == 'sweet':
#     print(Sentence[-1] + '?')


# sentence = input()
# person = 'sweet'
# if person == 'sweet':
#     space = sentence.rfind(' ')
#     if space == -1:
#         print(sentence[:] + '?')
#     else:
#         print(sentence[space+1:] + '?')


class SweetGuy:
    def __init__(self, name):
        self.name = name

    def reply(self, statement):
        temp = list(statement.split())
        print(statement)
        print(f'{self.name}: {temp[-1]}?')
        pass



p1 = SweetGuy('서상균')
statement1 = '어이가 없네요'
statement2 = '없네요?한다'
p1.reply(statement1)
p1.reply(statement2)