from commandtype import CommandType
import sys

comp_lst_a0 = ['0', '1', '-1', 'D', 'A', '!D', '!A', 'D+1',
               'A+1', 'D-1', 'A-1', 'D+A', 'D-A', 'A-D', 'D&A', 'D|A']
comp_lst_a1 = ['M', '!M', 'M+1', 'M-1', 'D+M', 'D-M', 'M-D', 'D&M', 'D|M']
dest_lst = ['null', 'M', 'D', 'MD', 'A', 'AM', 'AD', 'AMD']
jump_lst = ['null', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']


class Parser:
    def __init__(self, text):
        self.text = text.replace(' ', '')
        self.commandType = None
        self.rawVal = None
        self.dest = None
        self.comp = None
        self.jump = None

    def is_command(self):
        if self.text[0:2] == '//':  # コメントはコマンドではない
            return False
        elif self.text.strip() == '':  # 空白行はコマンドではない
            return False

        # print(self.text)
        return True

    def get_command_type(self):
        if self.is_command():
            if self.text[0] == '@':
                if isValOrSymbol(self.text[1:]):
                    self.commandType = CommandType.A_COMMAND
                    return CommandType.A_COMMAND
                else:
                    # print('Error, value must be sipecified characters',
                    #      file=sys.stderr)
                    return -1
            elif self.text[0] == '(' and isValOrSymbol(self.text[1:-1]) and self.text[-1] == ')':
                self.commandType = CommandType.L_COMMAND
                return CommandType.L_COMMAND
            else:
                dest = None
                comp = None
                jump = None
                if '=' in self.text and ';' in self.text and (self.text.find('=') < self.text.find(';')):
                    dest, comp_jump = self.text.split('=')
                    comp, jump = comp_jump.split(';')
                    if dest in dest_lst and (comp in comp_lst_a0 or comp in comp_lst_a1) and jump in jump_lst:
                        return CommandType.C_COMMAND

                elif '=' in self.text and ';' not in self.text:
                    dest, comp = self.text.split('=')
                    if dest in dest_lst and (comp in comp_lst_a0 or comp in comp_lst_a1):
                        return CommandType.C_COMMAND

                elif ';' in self.text and '=' not in self.text:
                    comp, jump = self.text.split(';')
                    if (comp in comp_lst_a0 or comp in comp_lst_a1) and jump in jump_lst:
                        return CommandType.C_COMMAND

                # print('Error, C_COMMAND parse error', file=sys.stderr)
                return -1

        # print('Error, this is not command', file=sys.stderr)
        return -1

    def get_symbol(self):
        if self.get_command_type() == CommandType.L_COMMAND:
            symbolText = self.text[1:-1]
            return symbolText
        elif self.get_command_type() == CommandType.A_COMMAND:
            return self.text[1:]

        # print("Error, command type is not L_COMMAND", file=sys.stderr)
        return -1

    def getDest(self):
        if self.get_command_type() == CommandType.C_COMMAND:
            if '=' in self.text:
                dest, _ = self.text.split('=')
                return dest
            else:
                # print(
                #     f'Error, dest not found in this C_COMMAND \"{self.text}\"')
                return 'null'
        else:
            # print('getDest function enable only C_COMMAND')
            return -1

    def getComp(self):
        if self.get_command_type() == CommandType.C_COMMAND:
            comp = None
            if '=' in self.text and ';' in self.text:
                _, comp_jump = self.text.split('=')
                comp, _ = comp_jump.split(';')
                return comp
            elif '=' in self.text:
                _, comp = self.text.split('=')
                return comp
            elif ';' in self.text:
                comp, _ = self.text.split(';')
                return comp
            else:
                return -1
        else:
            # print('getComp function enable only C_COMMAND')
            return -1

    def getJump(self):
        if self.get_command_type() == CommandType.C_COMMAND:
            jump = None
            if '=' in self.text and ';' in self.text:
                _, comp_jump = self.text.split('=')
                _, jump = comp_jump.split(';')
                return jump
            elif ';' in self.text:
                _, jump = self.text.split(';')
                return jump
            else:
                return 'null'
        else:
            # print('getJump function enable only C_COMMAND')
            return -1


def isValOrSymbol(rawText):
    if not rawText.isdigit():  # symbol
        if rawText[0].isdigit():
            return False  # 先頭が数字から始まるシンボルは使えない
        else:
            for c in rawText:
                if not (c.isalpha() or c.isdigit() or c == '.' or c == '$' or c == ':' or c == '_'):
                    return False

            return True

    return rawText.isdigit()  # value
