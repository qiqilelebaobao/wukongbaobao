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

        digit = (1, 10)

        if level == 1:
            pass
        elif level == 2:
            digit = (1, 20)
        else:
            print('Wrong position..')

        while True:
            question = Question.generate_question(algorithm, *digit)
            self.questions.add(question)

            if len(self.questions) >= cnt:
                break

        return self.questions

