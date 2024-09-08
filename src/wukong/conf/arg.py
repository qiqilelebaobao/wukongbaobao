import argparse
import sys

def init_arg():
    '''parse parameter from command line.'''
    
    parser = argparse.ArgumentParser(prog='python3 exam.py', description='This is a exam program for student.', epilog='Enjoy the exam. :) ')

    parser.add_argument('--level', '-l', help='level', default=1, type=int, choices=range(1, 10))
    parser.add_argument('--basic_cnt', '-bc', help='basic question count', default=25, type=int)
    parser.add_argument('--open_cnt', '-oc', help='open question count', default=0, type=int)
    parser.add_argument('--algorithm', '-a', help='algorithm', default='+', choices=['+', '-'])
    parser.add_argument('--version', '-v', action='version')

    parser.version = '1.0.0'

    args = parser.parse_args()

    if args.basic_cnt < 0 or args.open_cnt < 0:
        print('Count shall be positive.')
        sys.exit(-1)

    return args.level, args.basic_cnt, args.open_cnt, args.algorithm
