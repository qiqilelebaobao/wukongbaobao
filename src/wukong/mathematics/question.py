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
    def generate_open_question(i, e, algorithm):
        plus_context = (f'{i + 1}. 今天上午家里收到 {e[0]} 个快递，下午收到 {e[2]} 个快递，总共收到(   ) 个快递。', 
                   f'{i + 1}. 小明今天读了 {e[0]} 本绘本，昨天读了 {e[2]} 本绘本，小明今天和昨天总共读了(   ) 本绘本。',
                   f'{i + 1}. 弟弟今年 {e[0]} 岁， {e[2]} 年后，他是(   ) 岁。',
                   f'{i + 1}. 幼儿园有 {e[0]} 个小朋友在玩游戏，这个时候有 {e[2]} 个小朋友一起加入了游戏，现在有(   ) 个小朋友在玩游戏。',
                   f'{i + 1}. 我上个月吃了 {e[0]} 个冰激凌，这个月又吃了 {e[2]} 个冰激凌，总共吃了(   ) 个冰激凌。',
                   f'{i + 1}. 黑猫捉了 {e[0]} 只老鼠，花猫捉的老鼠比黑猫捉的多 {e[2]} 只 ，花猫捉了 (   ) 只老鼠。',
                   f'{i + 1}. 动物园里有 {e[0]} 只公鸭，还有 {e[2]} 只母鸭，动物园一共 有(   ) 只鸭子。',
                   f'{i + 1}. 爸爸在排队买火车票，爸爸排在队尾，前面有 {e[0]} 个人，这一队共有(   ) 人。',
                   f'{i + 1}. 妈妈在排队买汽车票，妈妈排在队首，后面有 {e[0]} 个人，这一队共有(   ) 人。',
                   f'{i + 1}. 奥特曼打败了 {e[0]} 只怪兽，使用技能后又打败了 {e[2]} 只怪兽，总共打败了 (   ) 只怪兽。',
                   f'{i + 1}. 小外公家门口种了两排白菜，其中一排种了 {e[0]} 颗，另一排种了 {e[2]} 颗，小外公家门口总共种了 (   ) 颗白菜。',
                   f'{i + 1}. 我上个月买了 {e[0]} 个棒棒糖，这个月又买了 {e[2]} 个棒棒糖，两个月总计买了 (   ) 个棒棒糖。',
                   f'{i + 1}. 琪琪跳绳，第一次跳了 {e[0]} 个，第二次跳了了 {e[2]} 个，两次一共跳了 (   ) 个。',
                   )
        
        minus_context = (f'{i + 1}. 妈妈让我去楼下小卖部买一瓶酱油， 酱油 {e[2]} 块钱，我给了小卖部阿姨 {e[0]} 块钱，她要找我 (   ) 块钱。', 
                   f'{i + 1}. 星期六我和爸爸妈妈去超市买了 {e[0]} 瓶酸奶，我们已经喝了 {e[2]} 瓶酸奶，还剩下 (   ) 瓶酸奶。',
                   f'{i + 1}. 公园树上有 {e[0]} 只小鸟，飞走了 {e[2]} 只小鸟，树上还有 (   ) 只小鸟。',
                   f'{i + 1}. 家里有 {e[0]} 个苹果，外婆吃了 {e[2]} 个苹果，还有 (   ) 个苹果。',
                   f'{i + 1}. 羊圈里有 {e[0]} 只小羊， 跑出了 {e[2]} 只， 羊圈里还剩下 (   ) 只小羊。',
                   )

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
