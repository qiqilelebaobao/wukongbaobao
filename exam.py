'''This a exam test for kids.
'''

from wukong.mathematics.question import Question
from wukong.view.printer import Printer
from wukong.conf.arg import init_arg

def main():

    cnt, level = init_arg()

    m = Question()
    q = m.generate_questions(cnt, level)

    p = Printer()
    p.output(q, 'docx')

if __name__ == '__main__':
    main()
