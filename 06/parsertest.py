import parser
from commandtype import CommandType


def test_is_command_comment():
    # -- is_command function test --
    # comment
    p = parser.Parser('// this is comment')
    assert not p.is_command()


def test_is_command_skip_space():
    # skip space rows
    p = parser.Parser('\t    \n    \t')
    assert not p.is_command()


def test_is_command_command_find():
    # command found test
    p = parser.Parser('D=M+1')
    assert p.is_command()


def test_get_command_type_value_test():
    # -- get_command_type test --
    # A_COMMAND value test
    p = parser.Parser('@42')
    assert p.get_command_type() == CommandType.A_COMMAND


def test_get_command_type_symbol_test():
    # A_COMMAND symbol test
    p = parser.Parser('@symbol.$:ABCDE')
    assert p.get_command_type() == CommandType.A_COMMAND


def test_get_command_type_symbol_fail():
    # A_COMMAND failed test (specified characters not used)
    p = parser.Parser('@12symbol')  # symbol head must not be digit
    assert p.get_command_type(
    ) == -1


def test_get_command_type_L_COMMAND():
    # L_COMMAND test
    p = parser.Parser('(LOOP)')
    assert p.get_command_type() == CommandType.L_COMMAND


def test_get_command_type_L_COMMAND_lost_right_paren():
    # L_COMMAND Lost right paren
    p = parser.Parser('(LOOP')
    assert p.get_command_type() == -1


def test_get_command_type_L_COMMAND_lost_left_paren():
    # L_COMMAND Lost left paren
    p = parser.Parser('LOOP)')
    assert p.get_command_type() == -1


def test_get_command_type_L_COMMAND_lost_both_paren():
    # L_COMMAND Lost both paren
    p = parser.Parser('LOOP')
    assert p.get_command_type() == -1


def test_get_command_type_L_COMMAND_with_space():
    # L_COMMAND space contain command
    p = parser.Parser('( LOOP )')
    assert p.get_command_type(
    ) == CommandType.L_COMMAND


def test_get_command_type_L_COMMAND_lost_right_paren_with_space():
    # L_COMMAND Lost right paren space contain
    p = parser.Parser('( LOOP')
    assert p.get_command_type() == -1


def test_get_command_type_L_COMMAND_lost_left_paren_with_space():
    # L_COMMAND Lost left paren space contain
    p = parser.Parser('LOOP )')
    assert p.get_command_type() == -1


def test_get_command_type_C_COMMAND():
    # C_COMMAND test
    p = parser.Parser('D=M+1;JMP')
    assert p.get_command_type() == CommandType.C_COMMAND


def test_get_command_type_C_COMMAND_split_character_switched_fail():
    # C_COMMAND split character switched fail test, # need to fix!
    p = parser.Parser('D;M+1=JMP')
    assert p.get_command_type() == -1


def test_get_command_type_C_COMMAND_dest_comp_command():
    # C_COMMAND test dest, comp command
    p = parser.Parser('D=M+1')
    assert p.get_command_type() == CommandType.C_COMMAND


def test_get_command_type_C_COMMAND_comp_jump_command():
    # C_COMMAND test comp, jump command
    p = parser.Parser('M+1;JEQ')
    assert p.get_command_type() == CommandType.C_COMMAND


def test_get_command_type_C_COMMAND_with_space():
    # C_COMMAND test space contain command
    p = parser.Parser('D = M+1 ; JMP')
    assert p.get_command_type(
    ) == CommandType.C_COMMAND


# -- getDest test --
def test_getDest_get_dest_from_full_C_COMMAND():
    # getDest from full C_COMMAND
    p = parser.Parser('D=M+1;JMP')
    assert p.getDest() == 'D'


def test_getDest_get_dest_from_dest_comp_command():
    p = parser.Parser('D=M+1')
    assert p.getDest() == 'D'


def test_getDest_not_found_dest():
    p = parser.Parser('M+1;JMP')
    assert p.getDest() == -1


def test_getDest_not_C_COMMAND_error():
    p = parser.Parser('@42')
    assert p.getDest() == -1


def test_getComp_get_comp_from_full_C_COMMAND():
    p = parser.Parser('D=M+1;JMP')
    assert p.getComp() == 'M+1'


def test_getComp_get_comp_from_dest_comp_command():
    p = parser.Parser('D=M+1')
    assert p.getComp() == 'M+1'


def test_getComp_get_comp_from_comp_jump_command():
    p = parser.Parser('M+1;JMP')
    assert p.getComp() == 'M+1'


def test_getJump_get_jump_from_full_C_COMMAND():
    p = parser.Parser('D=M+1;JMP')
    assert p.getJump() == 'JMP'


def test_getJump_get_jump_from_comp_jump_command():
    p = parser.Parser('M+1;JMP')
    assert p.getJump() == 'JMP'


def test_get_symbol_get_value_from_A_COMMAND():
    p = parser.Parser('@42')
    assert p.get_command_type() == CommandType.A_COMMAND
    assert p.get_symbol() == '42'


def test_get_symbol_get_value_from_L_COMMAND():
    p = parser.Parser('(42)')
    assert p.get_command_type() == CommandType.L_COMMAND
    assert p.get_symbol() == '42'


def test_get_symbol_get_symbol_from_A_COMMAND():
    p = parser.Parser('@R0')
    assert p.get_command_type() == CommandType.A_COMMAND
    assert p.get_symbol() == 'R0'


def test_get_symbol_get_symbol_from_L_COMMAND():
    p = parser.Parser('(LOOP)')
    assert p.get_command_type() == CommandType.L_COMMAND
    assert p.get_symbol() == 'LOOP'
