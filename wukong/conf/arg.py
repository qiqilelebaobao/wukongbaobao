import argparse

def init_arg():
    '''parse parameter from command line.'''
    
    parser = argparse.ArgumentParser(prog='python3 exam.py', description='This is a exam program for student.', epilog='Enjoy the exam. :) ')

    parser.add_argument('--cnt', help='count',default=25, type=int)
    parser.add_argument('--level', help='level', default=1, type=int, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    args = parser.parse_args()

    return args.cnt, args.level
