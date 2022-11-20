class SymbolTable:
    def __init__(self):
        self.symbolTable = {'SP': 0, 'LCL': 1, 'ARG': 2,
                            'THIS': 3, 'THAT': 4, 'SCREEN': 16384, 'KBD': 24576}
        for i in range(16):
            self.symbolTable['R' + str(i)] = i

    def addEntry(self, symbol, address):
        self.symbolTable[symbol] = address

    def contains(self, symbol):
        return symbol in self.symbolTable.keys()

    def getAddress(self, symbol):
        return self.symbolTable[symbol]

    def isAlreadyEntried(self, address):
        return address in self.symbolTable.values()
