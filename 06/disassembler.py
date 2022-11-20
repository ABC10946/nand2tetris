import sys


def disas_value(text):
    return str(int(text[1:], 2))


def comp_bin_to_mnemonic(a, comp_binary):
    mnemonic = ''
    if '101010' == comp_binary:
        mnemonic = '0'
    elif '111111' == comp_binary:
        mnemonic = '1'
    elif '111010' == comp_binary:
        mnemonic = '-1'
    elif '001100' == comp_binary:
        mnemonic = 'D'
    elif '110000' == comp_binary:
        mnemonic = 'A'
    elif '001101' == comp_binary:
        mnemonic = '!D'
    elif '110001' == comp_binary:
        mnemonic = '!A'
    elif '001111' == comp_binary:
        mnemonic = '-D'
    elif '110011' == comp_binary:
        mnemonic = '-A'
    elif '011111' == comp_binary:
        mnemonic = 'D+1'
    elif '110111' == comp_binary:
        mnemonic = 'A+1'
    elif '001110' == comp_binary:
        mnemonic = 'D-1'
    elif '110010' == comp_binary:
        mnemonic = 'A-1'
    elif '000010' == comp_binary:
        mnemonic = 'D+A'
    elif '010011' == comp_binary:
        mnemonic = 'D-A'
    elif '000111' == comp_binary:
        mnemonic = 'A-D'
    elif '000000' == comp_binary:
        mnemonic = 'D&A'
    elif '010101' == comp_binary:
        mnemonic = 'D|A'

    if a == '1':
        mnemonic = mnemonic.replace('A', 'M')

    return mnemonic


def dest_bin_to_mnemonic(dest_binary):
    if '000' == dest_binary:
        return 'null'
    elif '001' == dest_binary:
        return 'M'
    elif '010' == dest_binary:
        return 'D'
    elif '011' == dest_binary:
        return 'MD'
    elif '100' == dest_binary:
        return 'A'
    elif '101' == dest_binary:
        return 'AM'
    elif '110' == dest_binary:
        return 'AD'
    elif '111' == dest_binary:
        return 'AMD'


def jump_bin_to_mnemonic(jump_binary):
    if '000' == jump_binary:
        return 'null'
    elif '001' == jump_binary:
        return 'JGT'
    elif '010' == jump_binary:
        return 'JEQ'
    elif '011' == jump_binary:
        return 'JGE'
    elif '100' == jump_binary:
        return 'JLT'
    elif '101' == jump_binary:
        return 'JNE'
    elif '110' == jump_binary:
        return 'JLE'
    elif '111' == jump_binary:
        return 'JMP'


def main():
    for text in sys.stdin:
        text = text.strip()
        if text[0] == '0':
            print('@' + disas_value(text))
        elif text[0:3] == '111':
            a = text[3]
            comp = text[4:10]
            comp_mnemonic = comp_bin_to_mnemonic(a, comp)

            dest = text[10:13]
            dest_mnemonic = dest_bin_to_mnemonic(dest)

            jump = text[13:16]
            jump_mnemonic = jump_bin_to_mnemonic(jump)

            if dest_mnemonic == 'null':
                print(comp_mnemonic + ';' + jump_mnemonic)
            elif jump_mnemonic == 'null':
                print(dest_mnemonic + '=' + comp_mnemonic)
            else:
                print(dest_mnemonic + '=' + comp_mnemonic + ';' + jump_mnemonic)


if __name__ == '__main__':
    main()
