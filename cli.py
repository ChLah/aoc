from argparse import ArgumentParser
from datetime import date
from importlib import import_module
from framework.generate import load_challenge_files

def main():
    today = date.today()

    parser = ArgumentParser(description='CLI for loading and submitting advent of code solutions')
    parser.add_argument('-d', '--day', type=int, default=today.day, help='Required: The day of the challenge, defaults to today')
    parser.add_argument('-y', '--year', type=int, default=today.year, help='Required: The year of the challenge, defaults to current year')

    subparsers = parser.add_subparsers(dest='command', required=True)

    loadparser = subparsers.add_parser('load', help='Loads the challenge files')
    loadparser.add_argument('-s', '--session', type=str, required=True, help='Required: The session id, can be found in your browser cookies')

    solveparser = subparsers.add_parser('solve', help='Solves the challenge')
    solveparser.add_argument('-p', '--part', type=int, default=1, choices=(1, 2), help='Required: The part of the challenge, defaults to 1')

    args = parser.parse_args()

    if args.day < 1 or args.day > 25:
        print('Day must be between 1 and 25')
        exit()

    if args.command == 'load':
        load_challenge_files(args.day, args.year, args.session)
    
    elif args.command == 'solve':
        if args.part < 1 or args.part > 2:
            print('Part must be 1 or 2')
            exit()
    
        solution = import_module(f'solutions.year{args.year}.day{args.day}.solution').Solution(args.day, args.year)
        solution.solve(args.part)


if __name__ == '__main__':
    main()