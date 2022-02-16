class Connector:
    """A class to represent a logic connector"""
    connectors = ['and', 'or', 'nand', 'nor', 'xor', '->', '<->']

    def __init__(self, connector, first_symbol, second_symbol):
        self.connector = connector
        self.first_symbol = first_symbol
        self.second_symbol = second_symbol
        self.truth_table = []

        # evaluate symbol
        self.evaluate(connector)

    def __str__(self):
        return f'{self.second_symbol} {self.connector} {self.second_symbol}'

    def __repr(self):
        return f'{self.second_symbol} {self.connector} {self.second_symbol}'

    def evaluate(self, connector):
        """Evaluate the logical connector"""
        if connector in self.connectors:
            return True
        raise Exception('No valid connector')

    def define_connector(self):
        match self.connector:
            case 'and':
                And(self.connector, self.first_symbol, self.second_symbol)
            case 'or':
                And(self.connector, self.first_symbol, self.second_symbol)
            case 'nand':
                And(self.connector, self.first_symbol, self.second_symbol)
            case 'nor':
                And(self.connector, self.first_symbol, self.second_symbol)
            case 'xor':
                And(self.connector, self.first_symbol, self.second_symbol)
            case '->':
                And(self.connector, self.first_symbol, self.second_symbol)
            case '<->':
                And(self.connector, self.first_symbol, self.second_symbol)


class And(Connector):
    """A class to represent the and connector"""

    def __init__(self, connector, first_symbol, second_symbol):
        super().__init__(connector, first_symbol, second_symbol)

    def get_truth_table(self, first_symbol, second_symbol):
        self.truth_table = [first_symbol.truth_table[i] and second_symbol.truth_table[i]
                            for i in range(len(first_symbol.truth_table))]


class Or(Connector):
    """A class to represent the or connector"""

    def __init__(self, connector, first_symbol, second_symbol):
        super().__init__(connector, first_symbol, second_symbol)

    def get_truth_table(self, first_symbol, second_symbol):
        self.truth_table = [first_symbol.truth_table[i] or second_symbol.truth_table[i] for i in range(len(first_symbol.truth_table))]


class Xor(Connector):
    """A class to represent the xor connector"""

    def __init__(self, connector, first_symbol, second_symbol):
        super().__init__(connector, first_symbol, second_symbol)

    def get_truth_table(self, first_symbol, second_symbol):
        self.truth_table = [first_symbol.truth_table[i] != second_symbol.truth_table[i]
                            for i in range(len(first_symbol.truth_table))]


class Nor(Connector):
    """A class to represent the nor connector"""

    def __init__(self, connector, first_symbol, second_symbol):
        super().__init__(connector, first_symbol, second_symbol)

    def get_truth_table(self, first_symbol, second_symbol):
        self.truth_table = [not (first_symbol.truth_table[i] or second_symbol.truth_table[i])
                            for i in range(len(first_symbol.truth_table))]


class Nand(Connector):
    """A class to represent the nand connector"""

    def __init__(self, connector, first_symbol, second_symbol):
        super().__init__(connector, first_symbol, second_symbol)

    def get_truth_table(self, first_symbol, second_symbol):
        self.truth_table = [not (first_symbol.truth_table[i] and second_symbol.truth_table[i])
                            for i in range(len(first_symbol.truth_table))]


class SimpleImplication(Connector):
    """A class to represent the Simple implication connector"""

    def __init__(self, connector, first_symbol, second_symbol):
        super().__init__(connector, first_symbol, second_symbol)

    def get_truth_table(self, first_symbol, second_symbol):
        self.truth_table = [
            (first_symbol.truth_table[i] == second_symbol.truth_table[i] or (not first_symbol[i] and second_symbol[i]))
            for i in range(len(first_symbol.truth_table))]


class DoubleImplication(Connector):
    """A class to represent the Double implication connector"""

    def __init__(self, connector, first_symbol, second_symbol):
        super().__init__(connector, first_symbol, second_symbol)

    def get_truth_table(self, first_symbol, second_symbol):
        self.truth_table = [(first_symbol.truth_table[i] == second_symbol.truth_table[i])
                            for i in range(len(first_symbol.truth_table))]


class Negation:
    """A class to represent a logic negation"""

    def __init__(self, negation, symbol):
        self.symbol = symbol
        self.negation = negation
        self.truth_table = []

    def get_truth_table(self, symbol):
        self.truth_table = [not symbol.truth_table[i] for i in range(len(symbol.truth_table))]
