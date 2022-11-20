import coder


def test_dest_null_mnemonic():
    assert coder.dest('null') == [0, 0, 0]


def test_dest_memory_mnemonic():
    assert coder.dest('M') == [0, 0, 1]


def test_dest_D_Register_mnemonic():
    assert coder.dest('D') == [0, 1, 0]


def test_dest_A_Register_mnemonic():
    assert coder.dest('A') == [1, 0, 0]


def test_dest_AMD_Register_mnemonic():
    assert coder.dest('AMD') == [1, 1, 1]


def test_jump_null_mnemonic():
    assert coder.jump('null') == [0, 0, 0]


def test_jump_JGT_mnemonic():
    assert coder.jump('JGT') == [0, 0, 1]


def test_jump_JEQ_mnemonic():
    assert coder.jump('JEQ') == [0, 1, 0]


def test_jump_JGE_mnemonic():
    assert coder.jump('JGE') == [0, 1, 1]


def test_jump_JLT_mnemonic():
    assert coder.jump('JLT') == [1, 0, 0]


def test_jump_JNT_mnemonic():
    assert coder.jump('JNE') == [1, 0, 1]


def test_jump_JLE_mnemonic():
    assert coder.jump('JLE') == [1, 1, 0]


def test_jump_JMP_mnemonic():
    assert coder.jump('JMP') == [1, 1, 1]


def test_comp_mnemonic():
    assert coder.comp('D+M') == [1, 0, 0, 0, 0, 1, 0]
