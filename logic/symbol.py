class Symbol:
    """A class to represent a logic symbol"""
    def __init__(self, symbol):
        self.symbol = symbol
        self.truth_table = None

        # evaluate if the symbol is valid
        self.evaluate(symbol)

    @staticmethod
    def evaluate(symbol):
        if len(symbol) == 1 and 'a' <= symbol <= 'z':
            return True
        raise Exception('No valid symbol')

    def __str__(self):
        return f'{self.symbol}'

    def __repr__(self):
        return f'{self.symbol}'

    def __iter__(self):
        return self

    def __eq__(self, other):
        return self.__str__() == other.__str__()


class SymbolSolved(Symbol):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.symbol = str(self.symbol)

    def evaluate(self, symbol):
        return True

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol
