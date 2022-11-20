#!/usr/bin/python3
import sys
import parser


def main():
    for c in sys.stdin:
        print(c, end='')
        parsed_data = parser.Parser(c)
        dest = parsed_data.getDest()
        comp = parsed_data.getComp()
        jump = parsed_data.getJump()
        print(f'dest={dest}, comp={comp}, jump={jump}')


if __name__ == '__main__':
    main()
