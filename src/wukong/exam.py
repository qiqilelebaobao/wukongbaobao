'''This a exam test for kids.
'''

if __name__ == '__main__':

    from .mathematics.question import Question
    from .view.printer import Printer
    from .conf.arg import init_arg

    def main():

        level, basic_cnt, open_cnt, algorithm = init_arg()

        m = Question()
        qs = m.generate_questions(level, basic_cnt, open_cnt, algorithm)

        p = Printer()
        p.output(qs, 'docx')

    main()
