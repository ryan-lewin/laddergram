import unittest
from word_ladder import legal_word

class TestLegalWord(unittest.TestCase):

    def test1_is_alpha(self):
        word = 'hello'
        self.assertEqual(legal_word(word), word)

    def test2_is_alpha(self):
        word = '$$hELLO999'
        self.assertEqual(legal_word(word), 'Invalid entry, try again: ')

    def test3_is_alpha(self):
        word = '1234567'
        self.assertEqual(legal_word(word), 'Invalid entry, please enter a word of the same length: ')


if __name__ == "__main__":
    unittest.main()