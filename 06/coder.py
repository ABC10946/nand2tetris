def dest(mnemonic):
    # dest_binary[0] -> A Register
    #            [1] -> D Register
    #            [2] -> Memory
    dest_binary = [0, 0, 0]
    if mnemonic == 'null':
        return dest_binary

    if 'M' in mnemonic:
        dest_binary[2] = 1

    if 'D' in mnemonic:
        dest_binary[1] = 1

    if 'A' in mnemonic:
        dest_binary[0] = 1

    return dest_binary


def comp(mnemonic):
    comp_binary = []
    if mnemonic == '0':
        comp_binary = [1, 0, 1, 0, 1, 0]

    if mnemonic == '1':
        comp_binary = [1, 1, 1, 1, 1, 1]

    if mnemonic == '-1':
        comp_binary = [1, 1, 1, 0, 1, 0]

    if mnemonic == 'D':
        comp_binary = [0, 0, 1, 1, 0, 0]

    if mnemonic == 'A' or mnemonic == 'M':
        comp_binary = [1, 1, 0, 0, 0, 0]

    if mnemonic == '!D':
        comp_binary = [0, 0, 1, 1, 0, 1]

    if mnemonic == '!A' or mnemonic == '!M':
        comp_binary = [1, 1, 0, 0, 0, 1]

    if mnemonic == '-D':
        comp_binary = [0, 0, 1, 1, 1, 1]

    if mnemonic == '-A' or mnemonic == '-M':
        comp_binary = [1, 1, 0, 0, 1, 1]

    if mnemonic == 'D+1':
        comp_binary = [0, 1, 1, 1, 1, 1]

    if mnemonic == 'A+1' or mnemonic == 'M+1':
        comp_binary = [1, 1, 0, 1, 1, 1]

    if mnemonic == 'D-1':
        comp_binary = [0, 0, 1, 1, 1, 0]

    if mnemonic == 'A-1' or mnemonic == 'M-1':
        comp_binary = [1, 1, 0, 0, 1, 0]

    if mnemonic == 'D+A' or mnemonic == 'D+M':
        comp_binary = [0, 0, 0, 0, 1, 0]

    if mnemonic == 'D-A' or mnemonic == 'D-M':
        comp_binary = [0, 1, 0, 0, 1, 1]

    if mnemonic == 'A-D' or mnemonic == 'M-D':
        comp_binary = [0, 0, 0, 1, 1, 1]

    if mnemonic == 'D&A' or mnemonic == 'D&M':
        comp_binary = [0, 0, 0, 0, 0, 0]

    if mnemonic == 'D|A' or mnemonic == 'D|M':
        comp_binary = [0, 1, 0, 1, 0, 1]

    if 'M' in mnemonic:
        return [1] + comp_binary
    else:
        return [0] + comp_binary


def jump(mnemonic):
    # jump_binary[0] -> out < 0
    #            [1] -> out = 0
    #            [2] -> out > 0
    if mnemonic == 'null':
        return [0, 0, 0]

    if mnemonic == 'JGT':
        return [0, 0, 1]

    if mnemonic == 'JEQ':
        return [0, 1, 0]

    if mnemonic == 'JGE':
        return [0, 1, 1]

    if mnemonic == 'JLT':
        return [1, 0, 0]

    if mnemonic == 'JNE':
        return [1, 0, 1]

    if mnemonic == 'JLE':
        return [1, 1, 0]

    if mnemonic == 'JMP':
        return [1, 1, 1]
