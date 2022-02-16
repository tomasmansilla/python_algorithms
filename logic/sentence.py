from symbol import Symbol
from connectors import Connector, Negation


class Sentence:
    """A class to represent a logic sentence"""
    connectors = ['and', 'or', 'nand', 'nor', 'xor', '->', '<->']

    def __init__(self, sentence):
        """Initialize the sentence"""
        self.sentence = self.separate_parenthesis(sentence)
        self.sentence_connectors = []
        self.symbols = []
        # Create a new sentence which will contain symbols and connectors
        self.new_sentence = []

        # evaluate the sentence
        self.evaluate(self.sentence)
        # get the truth table for each symbol
        self.get_basis_truth_table(self.symbols)

    def __str__(self):
        return self.sentence

    def __repr__(self):
        return self.sentence

    def evaluate(self, sentence):
        """ evaluate the logical sentence"""
        if not sentence:
            raise Exception("nothing to evaluate")

        # check if sentence has balanced parenthesis
        if not self.balanced_parenthesis(sentence):
            raise Exception("parenthesis aren't balanced")

        # Convert the statement to a list to iterate over each element
        sentence_list = sentence.split()

        symbol = False
        connector = False
        negation = False

        for i in range(len(sentence_list)):
            if i == 0 or i == (len(sentence_list) - 1):
                if sentence_list[i] in self.connectors:
                    raise Exception('First or last elements can\'t be a connector')

            if self.is_symbol(sentence_list[i]):
                if symbol:
                    raise Exception('Two symbols together')
                else:
                    symbol = True
                    connector = False
                    negation = False
            elif self.is_connector(sentence_list[i]):
                if connector or negation:
                    raise Exception("Two connectors together")
                else:
                    connector = True
                    symbol = False
                    negation = False
            elif sentence_list[i] == 'not':
                negation = Negation(sentence_list[i])
                self.sentence_connectors.append(negation)
                self.new_sentence.append(negation)
                connector = False
                negation = True
                symbol = False
            elif sentence_list[i] == '(' or sentence_list[i] == ')':
                self.new_sentence.append(sentence_list[i])
            else:
                print(sentence_list[i])
                raise Exception('Invalid input')

    def is_symbol(self, char):
        """Evaluate if the char is a symbol"""
        if len(char) == 1 and 'a' <= char <= 'z':
            symbol = Symbol(char)
            if char not in self.symbols:
                self.symbols.append(symbol)

            self.new_sentence.append(symbol)
            return True

    def is_connector(self, char):
        """Evaluate if the char is a connector"""
        if char in self.connectors:
            connector = Connector(char)
            self.sentence_connectors.append(connector)
            self.new_sentence.append(connector)
            return True

    @staticmethod
    def balanced_parenthesis(sentence):
        """Check if a sentence has balanced parenthesis."""
        count = 0
        for ch in sentence:
            if ch == '(':
                count += 1
            elif ch == ')':
                if count <= 0:
                    return False
                count -= 1

            return count == 0

    @staticmethod
    def separate_parenthesis(sentence):
        """Add space between parenthesis."""
        new_sentence = ''
        for ch in sentence:
            if ch == '(' or ch == ')':
                new_sentence += f' {ch} '
            else:
                new_sentence += ch

        return new_sentence

    @staticmethod
    def get_basis_truth_table(symbols):
        # Truth tables has 2 raised to the n rows.
        # n = number of propositions
        n = len(symbols)
        numbers_rows = 2 ** n

        # get the truth values for each symbol
        for symbol in symbols:
            symbol_values = []

            # set number for divider
            divider = numbers_rows // (2 * 2 ** symbols.index(symbol))
            for n in range(numbers_rows):
                # calc if the value should be true or false based on their position
                calc = n // divider
                if calc % 2 == 0:
                    symbol_values.append(True)
                else:
                    symbol_values.append(False)

            symbol.truth_table = symbol_values

    def calculate(self):
        """Calculate the final expression"""
        pass
