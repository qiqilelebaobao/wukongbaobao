'''This a exam test for kids.
'''

from wukong.mathematics.question import Question
from wukong.view.printer import Printer
from wukong.conf.arg import init_arg

def main():

    level, basic_cnt, open_cnt, algorithm = init_arg()

    m = Question()
    qs = m.generate_questions(level, basic_cnt, open_cnt, algorithm)

    p = Printer()
    p.output(qs, 'docx')

if __name__ == '__main__':
    main()
