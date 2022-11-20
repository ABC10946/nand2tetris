import disassembler


def test_value():
    assert disassembler.disas_value('0000000000010111') == '23'
