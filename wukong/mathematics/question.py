from itertools import count
import random

class Question:
    '''Math Class'''
    count = 0
    def __init__(self, name = 'math', stage = 'K2'):
        Question.count += 1
        self.name = name
        self.stage = stage
        self.questions = set()
        self.dupquestion = 0

    def __str__(self):
        return f'{self.name=} {self.stage=}'
    
    @staticmethod
    def generate_question( algorithm = '+', min_digit = 1, max_digit = 10):

        question = random.randint(min_digit, max_digit), algorithm, random.randint(min_digit, max_digit)
        if algorithm == '-':
            a = question[0]
            b = question[2]
            if b > a:
                question = b, algorithm, a

        return question
    
    def generate_questions(self, cnt = 10,level = 1, algorithm = '+'):

        digit = (0, 10)

        if level == 1:
            pass
        elif level == 2:
            digit = (11, 20)
        elif level == 3:
            digit = (21, 30)
        elif level == 4:
            digit = (31, 40)
        elif level == 5:
            digit = (41, 50)
        elif level == 6:
            digit = (51, 60)
        elif level == 7:
            digit = (61, 70)
        elif level == 8:
            digit = (71, 80)
        elif level == 9:
            digit = (81, 90)
        elif level == 10:
            digit = (91, 100)     
        else:
            print('Wrong position..')

        while True:
            question = Question.generate_question(algorithm, *digit)
            self.questions.add(question)

            if len(self.questions) >= cnt:
                break

        return self.questions

