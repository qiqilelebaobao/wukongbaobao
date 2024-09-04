from itertools import count
import random

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
    def generate_open_question(i, e):
        context = (f'{i + 1}. 今天上午家里收到 {e[0]} 个快递，下午收到 {e[2]} 个快递，总共收到(   ) 个快递。', 
                   f'{i + 1}. 今天读了 {e[0]} 本绘本，昨天读了 {e[2]} 本绘本，总共读了(   ) 本绘本。',
                   f'{i + 1}. 弟弟今年 {e[0]} 岁， {e[2]} 年后，他是(   ) 岁。',
                   f'{i + 1}. 幼儿园有 {e[0]} 个小朋友在玩游戏，这个时候有 {e[2]} 个小朋友一起加入了游戏，现在有(   ) 个小朋友在玩游戏。',
                   f'{i + 1}. 我上个月吃了 {e[0]} 个冰激凌，这个月又吃了 {e[2]} 个冰激凌，总共吃了(   ) 个冰激凌。',
                   f'{i + 1}. 黑猫捉了 {e[0]} 只老鼠，花猫捉的老鼠比黑猫捉的多 {e[2]} 只 ，花猫捉了 (   ) 只老鼠。',
                   f'{i + 1}. 动物园里有 {e[0]} 只公鸭，还有 {e[2]} 只母鸭，动物园一共 有(   ) 只鸭子。',
                   f'{i + 1}. 爸爸在排队买票，爸爸排在队尾，前面有 {e[0]} 个人，这一队共有(   ) 人。',
                   f'{i + 1}. 妈妈在排队买票，妈妈排在队首，后面有 {e[0]} 个人，这一队共有(   ) 人。',
                   )

        return random.choice(context)

    @staticmethod
    def generate_basic_question(i, e):
        question = f'{i + 1}.\t{e[0]:^3}{e[1]}{e[2]:^4} ='
        return question

    def generate_questions(self, level = 1, basic_cnt = 25, open_cnt = 0, algorithm = '+'):
        assert(basic_cnt >=0 and open_cnt >= 0)
        
        total = basic_cnt + open_cnt
        self.generate_digits(basic_cnt + open_cnt, level, algorithm)

        for i in range(basic_cnt):
            self.questions.append(Question.generate_basic_question(i, self.digits_list[i]))
        
        for i in range(basic_cnt, total):
            self.questions.append(Question.generate_open_question(i, self.digits_list[i]))

        return self.questions
