import os
import sys


from wukongbaobao.mathematics.question import Question
from wukongbaobao.view.printer import Printer
from wukongbaobao.conf.arg import init_arg
from wukongbaobao.conf.output import init_output_dir

def main():

    level, basic_cnt, open_cnt, algorithm = init_arg()

    init_output_dir()

    m = Question()
    qs = m.generate_questions(level, basic_cnt, open_cnt, algorithm)

    p = Printer()
    name = p.output(qs, 'docx')
    
    feedback_template = f'''
Successfully generated "{name}" math tests:
The level is {level}, basic question {basic_cnt}, open questions {open_cnt}.
Please enjoy it.
'''

    print(feedback_template)

if __name__ == '__main__':

    main()
