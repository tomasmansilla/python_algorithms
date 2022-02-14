import plotly.graph_objects as pl


# represent the sentence
class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.propositions = self.get_propositions(self.sentence)
        self.symbols = []
        self.fig = self.set_truth_table_basis(self.propositions)

    def __repr__(self):
        return self.sentence

    def __str__(self):
        return self.sentence

    # Get propositions from the sentence
    @staticmethod
    def get_propositions(sentence):
        props = list({letter for letter in sentence if 'a' < letter < 'z'})
        return sorted(props)

    # create symbol for proposition
    def make_symbol(self, symbol, values):
        self.symbols.append(Symbol(symbol, values))

    # make the true table
    def set_truth_table_basis(self, props):
        # true table has 2 a la n rows
        n = len(props)
        amount_row = 2 ** n

        # body table
        total_values = []
        for prop in props:
            values = []

            # set number for divider
            divider = amount_row // (2 * 2 ** props.index(prop))

            for n in range(amount_row):
                # calc if should be true or false
                calc = n // divider
                if calc % 2 == 0:
                    values.append(True)
                else:
                    values.append(False)

            total_values.append(values)
            self.make_symbol(prop, values)

        # table
        fig = pl.Figure(data=[pl.Table(
            header=dict(values=props), cells=dict(values=total_values)
        )])

        return fig

    # show the truth table
    def show_truth_table(self):
        self.fig.show()

    # show all the symbols of the sentence
    def show_symbols(self):
        return self.symbols

    # conjunction logic
    @staticmethod
    def conjunction(first_symbol, second_symbol):
        result = And(first_symbol, second_symbol)
        return result


# represent a simple proposition
class Symbol:
    def __init__(self, symbol, truth_values):
        self.symbol = symbol
        self.truth_values = truth_values

        # set items
        self.__setitems__()

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol

    def __len__(self):
        return len(self.truth_values)

    def __setitems__(self):
        self.values = ['Value'] * len(self)
        for i in range(len(self)):
            self.__setitem__(i, self.truth_values[i])

    def __setitem__(self, key, value):
            self.values[key] = value

    def __getitem__(self, item):
            return self.values[item]

    def get_truth_value(self):
        return self.truth_values


# represent a model for logical connective
class LogicalConnective:
    def __init__(self, first_symbol, second_symbol):
        self.first_symbol = first_symbol
        self.second_symbol = second_symbol
        self.truth_value = ['Value'] * len(self.first_symbol)
        self.results = ['Value'] * len(self.first_symbol)
        self.fig = None

        # set all items
        self.__setitems__()

        # create the truth table

    def set_truth_table(self, results, symbol_string):
        self.__setitems__()
        fig = pl.Figure(data=[pl.Table(
            header=dict(values=[f'{self.first_symbol} {symbol_string} {self.second_symbol}']),
            cells=dict(values=[results])
        )])
        return fig

    def __setitems__(self):
        for i in range(len(self.results)):
            self.__setitem__(i, self.results[i])

    def __setitem__(self, key, value):
        self.truth_value[key] = value

    def __getitem__(self, item):
        return self.truth_value[item]

    def __str__(self):
        return self.results

    def __repr__(self):
        return self.results

    # show truth table of the conjunction of first_symbol and second_symbol
    def show_truth_table(self):
        self.fig.show()


# represent logical conjunction
class And(LogicalConnective):
    def __init__(self, first_symbol, second_symbol):
        super().__init__(first_symbol, second_symbol)
        self.results = self.get_results(self.first_symbol, self.second_symbol)
        self.fig = self.set_truth_table(self.results, '^')

    # get the results of the conjunction
    @staticmethod
    def get_results(first_symbol, second_symbol):
        results = [first_symbol[i] and second_symbol[i] for i in range(len(first_symbol))]
        return results


# represent a logical disjunction
class Or(LogicalConnective):
    def __init__(self, first_symbol, second_symbol):
        super().__init__(first_symbol, second_symbol)
        self.results = self.get_results(self.first_symbol, self.second_symbol)
        self.fig = self.set_truth_table(self.results, 'or')

    # get the results of the disjunction
    @staticmethod
    def get_results(first_symbol, second_symbol):
        results = [first_symbol[i] or second_symbol[i] for i in range(len(first_symbol))]
        return results


# represent logic or exclusive
class Xor(LogicalConnective):
    def __init__(self, first_symbol, second_symbol):
        super().__init__(first_symbol, second_symbol)
        self.results = self.get_results(self.first_symbol, self.second_symbol)
        self.fig = self.set_truth_table(self.results, 'xor')

    # get the results of the xor
    @staticmethod
    def get_results(first_symbol, second_symbol):
        results = [first_symbol[i] != second_symbol[i] for i in range(len(first_symbol))]
        return results


# represent nor logic gate
class Nor(LogicalConnective):
    def __init__(self, first_symbol, second_symbol):
        super().__init__(first_symbol, second_symbol)
        self.results = self.get_results(self.first_symbol, self.second_symbol)
        self.fig = self.set_truth_table(self.results, 'nor')

    # get the results of the xor
    @staticmethod
    def get_results(first_symbol, second_symbol):
        results = [not (first_symbol[i] or second_symbol[i]) for i in range(len(first_symbol))]
        return results


# represent nand logic gate
class Nand(LogicalConnective):
    def __init__(self, first_symbol, second_symbol):
        super().__init__(first_symbol, second_symbol)
        self.results = self.get_results(self.first_symbol, self.second_symbol)
        self.fig = self.set_truth_table(self.results, 'nor')

    # get the results of the xor
    @staticmethod
    def get_results(first_symbol, second_symbol):
        results = [not (first_symbol[i] and second_symbol[i]) for i in range(len(first_symbol))]
        return results


# represent a logic negation
class No(LogicalConnective):
    def __init__(self, symbol):
        super().__init__(symbol, None)
        self.results = self.get_results(self.first_symbol)
        self.fig = self.set_truth_table(self.results, '~')

    # get the results of the negation
    @staticmethod
    def get_results(first_symbol):
        results = [not first_symbol[i] for i in range(len(first_symbol))]
        return results

    def set_truth_table(self, results, symbol_string):
        fig = pl.Figure(data=[pl.Table(
            header=dict(values=[f'{symbol_string}{self.first_symbol}']),
            cells=dict(values=[results])
        )])
        return fig


# represent a simple implication
class SimpleImplication(LogicalConnective):
    def __init__(self, first_symbol, second_symbol):
        super().__init__(first_symbol, second_symbol)
        self.results = self.get_results(self.first_symbol, self.second_symbol)
        self.fig = self.set_truth_table(self.results, '->')

    # get the results of the simple implication
    @staticmethod
    def get_results(first_symbol, second_symbol):
        results = [(first_symbol[i] == second_symbol[i] or (not first_symbol[i] and second_symbol[i]))
                   for i in range(len(first_symbol))]
        return results


# represent a double implication
class DoubleImplication(LogicalConnective):
    def __init__(self, first_symbol, second_symbol):
        super().__init__(first_symbol, second_symbol)
        self.results = self.get_results(self.first_symbol, self.second_symbol)
        self.fig = self.set_truth_table(self.results, '<->')

    # get the results of the simple implication
    @staticmethod
    def get_results(first_symbol, second_symbol):
        results = [(first_symbol[i] == second_symbol[i])
                   for i in range(len(first_symbol))]
        return results


# script principal
def test():
    phrase = 'p q r'
    mi_phrase = Sentence(phrase)


# run script
test()
