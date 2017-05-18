import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It will most likely happen'
    elif answerNumber == 2:
        return 'Its possible'
    elif answerNumber == 3:
        return 'Of course'
    elif answerNumber == 4:
        return 'Nope'
    elif answerNumber == 5:
        return 'Lets say maybe'
    elif answerNumber == 6:
        return 'Yikes... umm things look good dont worry about it'
    elif answerNumber == 7:
        return 'I wouldnt go outside today'
    elif answerNumber == 8:
        return 'What a lucky looking day'
    elif answerNumber == 9:
        return 'Im not so certain ask again at a later time'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
