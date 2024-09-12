import os
import sys


if not __package__:
    # Make CLI runnable from source tree with
    #    python src/package

    from mathematics.question import Question
    from view.printer import Printer
    from conf.arg import init_arg

    package_source_path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, package_source_path)

else:
    from .mathematics.question import Question
    from .view.printer import Printer
    from .conf.arg import init_arg

if __name__ == '__main__':

    def main():

        level, basic_cnt, open_cnt, algorithm = init_arg()

        m = Question()
        qs = m.generate_questions(level, basic_cnt, open_cnt, algorithm)

        p = Printer()
        p.output(qs, 'docx')

    main()
