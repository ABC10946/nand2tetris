import symboltable


def test_symboltable_initialized():
    st = symboltable.SymbolTable()
    assertSymbolTable = {'SP': 0, 'LCL': 1, 'ARG': 2,
                         'THIS': 3, 'THAT': 4, 'SCREEN': 16384, 'KBD': 24576, 'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15}

    for key in assertSymbolTable.keys():
        assert st.symbolTable[key] == assertSymbolTable[key]


def test_add_new_symbol():
    st = symboltable.SymbolTable()
    st.addEntry('LOOP', 512)
    assert st.symbolTable['LOOP'] == 512


def test_contain():
    st = symboltable.SymbolTable()
    st.addEntry('TEST_SYMBOL1', 513)
    assert st.contains('TEST_SYMBOL1')


def test_getAddress():
    st = symboltable.SymbolTable()
    st.addEntry('TEST_SYMBOL2', 514)
    assert st.getAddress('TEST_SYMBOL2') == 514
