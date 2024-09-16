from itertools import count
import random

from .template import plus_level_1_context, minus_level_1_context

class Question:
    '''Math Class'''
    count = 0
    def __init__(self, name = 'math', stage = 'K2'):
        Question.count += 1
        self.name = name
        self.stage = stage
        self.digits = set()
        self.digits_list = []
        self.questions = []
        self.dupquestion = 0

    def __str__(self):
        return f'{self.name=} {self.stage=}'
    
    @staticmethod
    def generate_digit( algorithm = '+', min_digit = 1, max_digit = 10):

        digits = random.randint(min_digit, max_digit), algorithm, random.randint(min_digit, max_digit)
        if algorithm == '-':
            a = digits[0]
            b = digits[2]
            if b > a:
                digits = b, algorithm, a

        return digits
    
    def generate_digits(self, cnt, level, algorithm):

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
            question = Question.generate_digit(algorithm, *digit)
            self.digits.add(question)

            if len(self.digits) >= cnt:
                break
        
        self.digits_list = list(self.digits)

    @staticmethod
    def generate_open_question(i, e, algorithm):

        plus_context = [template.format(index = i + 1, augend=e[0], addend=e[2]) for template in plus_level_1_context]
        minus_context = [template.format(index = i + 1, minuend = e[0], subtrahend = e[2]) for template in minus_level_1_context]

        if algorithm == '+':
            return random.choice(plus_context)
        elif algorithm == '-':
            return random.choice(minus_context)
        else:
            print('wrong position.') 
            return 

    @staticmethod
    def generate_basic_question(i, e, algorithm):
        question = f'{i + 1}.\t{e[0]:^3}{e[1]}{e[2]:^4} ='
        return question

    def generate_questions(self, level = 1, basic_cnt = 25, open_cnt = 0, algorithm = '+'):
        assert(basic_cnt >=0 and open_cnt >= 0)
        
        total = basic_cnt + open_cnt
        self.generate_digits(basic_cnt + open_cnt, level, algorithm)

        for i in range(basic_cnt):
            self.questions.append(Question.generate_basic_question(i, self.digits_list[i], algorithm))
        
        for i in range(basic_cnt, total):
            self.questions.append(Question.generate_open_question(i, self.digits_list[i], algorithm))

        return self.questions
