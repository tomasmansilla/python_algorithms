from sentence import Sentence
from symbol import Symbol
from connectors import Connector


class Logic:
    """Overall class to manage program behavior"""

    def __init__(self, sentence):
        """Initialize the program"""
        pass


# Script principal
def test():
    # phrase = input('Enter the sentence: ')
    phrase = 'not and p or p'
    my_sentence = Sentence(phrase)
    print(my_sentence.symbols, my_sentence.new_sentence, my_sentence.sentence_connectors)


# Run script principal
test()
