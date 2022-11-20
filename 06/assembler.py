#!/usr/bin/python3
import sys
import parser
import coder


def main():
    for c in sys.stdin:
        parsed_data = parser.Parser(c)
        # print(c, end='')
        dest = parsed_data.getDest()
        comp = parsed_data.getComp()
        jump = parsed_data.getJump()
        symbol = parsed_data.get_symbol()
        # print(
        #     f'dest={dest}, comp={comp}, jump={jump}, symbol={symbol}')

        dest_binary = [0, 0, 0]
        comp_binary = [0, 0, 0, 0, 0, 0, 0]
        jump_binary = [0, 0, 0]
        symbol_binary = []

        if dest != -1:
            dest_binary = coder.dest(dest)
            # print('d', dest_binary)

        if comp != -1:
            comp_binary = coder.comp(comp)
            # print('c', comp_binary)

        if jump != -1:
            jump_binary = coder.jump(jump)
            # print('j', jump_binary)

        if symbol != -1:
            symbol_binary = valToBin(int(symbol))

        a_command_binary = symbol_binary
        c_command_binary_raw = comp_binary + dest_binary + jump_binary

        if a_command_binary != []:
            print(''.join(map(str, symbol_binary)))

        if sum(c_command_binary_raw) != 0:
            c_command_binary = [1, 1, 1] + c_command_binary_raw
            print(''.join(map(str, c_command_binary)))


def valToBin(val: int):
    binStr = bin(val)[2:]
    rawBin = list(map(int, binStr))

    paddingNum = 16 - len(rawBin)
    retBin = rawBin
    for _ in range(paddingNum):
        retBin = [0] + retBin

    return retBin


if __name__ == '__main__':
    main()
