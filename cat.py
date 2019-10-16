#!/usr/bin/python3

import argparse, logging, sys

__version__ = '0.0.1'

logging.basicConfig(level=logging.ERROR)

class Catter(object):

    def __init__(self, files, show_numbers=False):
        self.files = files
        self.show_numbers = show_numbers

    def run(self, fout):
        fmt = '{0:>6} {1}'
        count = 1
        for fin in self.files:
            logging.debug('catting {0}'.format(fin))
            for line in fin:
                if self.show_numbers:
                    fout.write(fmt.format(count, line))
                    count += 1
                else:
                    fout.write(line)

def main(args):
    parser = argparse.ArgumentParser(description='Concatenate FILE(s), or ''standard input, to standard output')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-n', '--number', action='store_true', help='number all output lines')
    parser.add_argument('files', nargs='*', type=argparse.FileType('r'),default=[sys.stdin], metavar='FILE')
    parser.add_argument('--run-test', action='store_true', help='run module tests')
    args = parser.parse_args(args)

    if args.run_test:
        import doctest
        doctest.testmod()
    else:
        cat = Catter(args.files, args.number)
        cat.run(sys.stdout)

if __name__ == '__main__':
    main(sys.argv[1:])

