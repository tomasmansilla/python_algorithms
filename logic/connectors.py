class Connector:
    """A class to represent a logic connector"""
    connectors = ['and', 'or', 'nand', 'nor', 'xor', '->', '<->']

    def __init__(self, connector):
        self.connector = connector
        self.first_symbol = ' '
        self.second_symbol = ' '
        self.truth_table = []

    def __str__(self):
        return f'{self.first_symbol} {self.connector} {self.second_symbol}'

    def __repr__(self):
        return f'{self.first_symbol} {self.connector} {self.second_symbol}'

    def define_connector(self):
        """ evaluate the connector parameter and define what kind of logic connector is"""
        match self.connector:
            case 'and':
                And(self.connector)
            case 'or':
                And(self.connector)
            case 'nand':
                And(self.connector)
            case 'nor':
                And(self.connector)
            case 'xor':
                And(self.connector)
            case '->':
                And(self.connector)
            case '<->':
                And(self.connector)


class And(Connector):
    """A class to represent the and connector"""

    def __init__(self, connector):
        """Initialize the connector"""
        super().__init__(connector)

    def get_truth_table(self, first_symbol, second_symbol):
        """get the truth table of the connector and set the symbols"""
        self.first_symbol = first_symbol
        self.second_symbol = second_symbol
        self.truth_table = [first_symbol.truth_table[i] and second_symbol.truth_table[i]
                            for i in range(len(first_symbol.truth_table))]


class Or(Connector):
    """A class to represent the or connector"""

    def __init__(self, connector):
        """Initialize the connector"""
        super().__init__(connector)

    def get_truth_table(self, first_symbol, second_symbol):
        """get the truth table of the connector and set the symbols"""
        self.first_symbol = first_symbol
        self.second_symbol = second_symbol
        self.truth_table = [first_symbol.truth_table[i] or second_symbol.truth_table[i] for i in range(len(first_symbol.truth_table))]


class Xor(Connector):
    """A class to represent the xor connector"""

    def __init__(self, connector):
        """Initialize the connector"""
        super().__init__(connector)

    def get_truth_table(self, first_symbol, second_symbol):
        """get the truth table of the connector and set the symbols"""
        self.first_symbol = first_symbol
        self.second_symbol = second_symbol
        self.truth_table = [first_symbol.truth_table[i] != second_symbol.truth_table[i]
                            for i in range(len(first_symbol.truth_table))]


class Nor(Connector):
    """A class to represent the nor connector"""

    def __init__(self, connector):
        """Initialize the connector"""
        super().__init__(connector)

    def get_truth_table(self, first_symbol, second_symbol):
        """get the truth table of the connector and set the symbols"""
        self.first_symbol = first_symbol
        self.second_symbol = second_symbol
        self.truth_table = [not (first_symbol.truth_table[i] or second_symbol.truth_table[i])
                            for i in range(len(first_symbol.truth_table))]


class Nand(Connector):
    """A class to represent the nand connector"""

    def __init__(self, connector):
        """Initialize the connector"""
        super().__init__(connector)

    def get_truth_table(self, first_symbol, second_symbol):
        """get the truth table of the connector and set the symbols"""
        self.truth_table = [not (first_symbol.truth_table[i] and second_symbol.truth_table[i])
                            for i in range(len(first_symbol.truth_table))]


class SimpleImplication(Connector):
    """A class to represent the Simple implication connector"""

    def __init__(self, connector):
        super().__init__(connector)

    def get_truth_table(self, first_symbol, second_symbol):
        """Get the truth table of the connector and set the symbols"""
        self.first_symbol = first_symbol
        self.second_symbol = second_symbol
        self.truth_table = [
            (first_symbol.truth_table[i] == second_symbol.truth_table[i] or (not first_symbol[i] and second_symbol[i]))
            for i in range(len(first_symbol.truth_table))]


class DoubleImplication(Connector):
    """A class to represent the Double implication connector"""

    def __init__(self, connector):
        """Initialize the connector"""
        super().__init__(connector)

    def get_truth_table(self, first_symbol, second_symbol):
        """get the truth table of the connector and set the symbols"""
        self.first_symbol = first_symbol
        self.second_symbol = second_symbol
        self.truth_table = [(first_symbol.truth_table[i] == second_symbol.truth_table[i])
                            for i in range(len(first_symbol.truth_table))]


class Negation:
    """A class to represent a logic negation"""

    def __init__(self, negation):
        """Initialize the logic negation"""
        self.symbol = None
        self.negation = negation
        self.truth_table = []

    def get_truth_table(self, symbol):
        """get the truth table of the connector"""
        self.symbol = symbol
        self.truth_table = [not symbol.truth_table[i] for i in range(len(symbol.truth_table))]

    def __str__(self):
        return f'~{self.symbol}'

    def __repr__(self):
        return f'~{self.symbol}'
