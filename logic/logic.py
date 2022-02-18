from sentence import Sentence
from symbol import Symbol, SymbolSolved
from connectors import Connector, Negation
import plotly.graph_objects as pl


class Logic:
    """Overall class to manage program behavior"""
    precedence_levels = 5

    def __init__(self, sentence):
        """Initialize the program"""
        self.sentence = Sentence(sentence)
        self.symbols = self.sentence.symbols
        self.connectors = self.sentence.sentence_connectors
        self.new_sentence = self.sentence.new_sentence
        self.fig = None

        # results
        self.symbols_solved = []
        self.results = []

        # set results
        self.check_sentence(self.new_sentence)
        self.set_results()
        self.set_table()

    def check_sentence(self, sentence):
        """Check the sentence"""
        new_sentence = []
        element_checked = False

        # Iter for precedence
        for n in range(1, self.precedence_levels+1):
            # Iter for element
            for elem in sentence:
                if elem == '(':
                    index_element = sentence.index(elem)
                    index_second_element = sentence.index(')', index_element)
                    result = self.is_parenthesis_open(sentence, elem)
                    new_sentence.append(result[0])
                    sentence[index_element:index_second_element+1] = result
                    self.symbols_solved.append(result[0])
                    element_checked = False
                elif elem == ')':
                    new_sentence.append(')')
                    a = self.is_parenthesis_close(new_sentence, elem)
                    a.symbol = f'({a.symbol[1:-1]})'
                    new_sentence = [a]
                    return new_sentence
                elif isinstance(elem, Negation):
                    if n == 1:
                        if self.is_negation(sentence, elem):
                            new_sentence.append(self.is_negation(sentence, elem))
                            element_checked = True
                        else:
                            new_sentence.append(elem)
                    else:
                        new_sentence.append(elem)
                elif isinstance(elem, Connector):
                    if elem.precedence == n and (not elem.solved):
                        if self.is_connector(sentence, elem):
                            new_sentence.pop()
                            new_sentence.append(self.is_connector(sentence, elem))
                            element_checked = True
                        else:
                            new_sentence.append(elem)
                    else:
                        new_sentence.append(elem)
                elif elem in self.symbols or elem in self.symbols_solved:
                    if element_checked:
                        element_checked = False
                    else:
                        new_sentence.append(self.is_symbol(elem))

            sentence = new_sentence
            new_sentence = []
            if len(sentence) == 1:
                break

        if len(sentence) != 1:
            self.check_sentence(sentence)
        else:
            symbol_solved = SymbolSolved(f'{sentence}')
            symbol_solved.truth_table = sentence[0].truth_table
            return symbol_solved

    def is_parenthesis_open(self, sentence, elem):
        """If element is parenthesis open execute this"""
        index_elem = sentence.index(elem)
        # index elem +1 para eliminar este parentesis de la sentencia
        new_sentence = sentence[index_elem+1:]
        sentence = self.check_sentence(new_sentence)
        return sentence

    def is_parenthesis_close(self, sentence, elem):
        """ If element is parenthesis close execute this."""
        index_elem = sentence.index(elem)
        return self.check_sentence(sentence[:index_elem])

    @staticmethod
    def is_symbol(elem):
        """ If element is symbol execute this"""
        return elem

    def is_connector(self, sentence, elem):
        """If element is connector execute this."""
        index_elem = sentence.index(elem)
        if sentence[index_elem+1] in self.symbols or sentence[index_elem+1] in self.symbols_solved:
            element_truth_table = elem.get_truth_table(sentence[index_elem-1], sentence[index_elem+1])
            symbol_solved = SymbolSolved(elem)
            symbol_solved.truth_table = element_truth_table
            self.symbols_solved.append(symbol_solved)
            self.results.append(symbol_solved)
            elem.solved = True
            return symbol_solved
        else:
            return False

    def is_negation(self, sentence, elem):
        """If element is negation execute this."""
        index_elem = sentence.index(elem)
        if sentence[index_elem+1] in self.symbols or sentence[index_elem+1] in self.symbols_solved:
            symbol_solved = SymbolSolved(f'{sentence[index_elem]} {sentence[index_elem+1]}')
            symbol_solved.truth_table = elem.get_truth_table(sentence[index_elem+1])
            self.symbols_solved.append(symbol_solved)
            self.results.append(symbol_solved)
            return symbol_solved
        else:
            return elem

    def __str__(self):
        return f'{self.sentence}'

    def set_results(self):
        results = []
        for result in self.results:
            if result in results:
                continue
            else:
                results.append(result)

        self.results = results

    def set_table(self):
        header = []
        body = []
        for symbol in self.symbols:
            header.append(str(symbol))
        for result in self.results:
            header.append(str(result))

        for symbol in self.symbols:
            body.append(list(symbol.truth_table))
        for result in self.results:
            body.append(list(result.truth_table))

        self.fig = pl.Figure(data=[pl.Table(header=dict(values=header), cells=dict(values=body))])

    def show_table(self):
        # self.fig.show()
        self.fig.show()


# Script principal
def test():
    # phrase = input('Enter the sentence: ')
    menu = (f'Hi \n'
            'Commands: not | and | or | -> | <->\n'
            'Enter your proposition: ')
    phrase = input(menu)
    my_sentence = Logic(phrase)
    my_sentence.show_table()


# Run script principal
test()
