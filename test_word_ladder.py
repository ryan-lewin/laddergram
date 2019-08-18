import unittest
from word_ladder import legal_word

class TestLegalWord(unittest.TestCase):
    def test1_is_alpha(self):
        word = 'hello'
        self.assertTrue(legal_word(word))

    def test2_is_alpha(self):
        word = '$$hELLO999'
        self.assertFalse(legal_word(word))

    def test3_is_alpha(self):
        word = '1234567'
        self.assertFalse(legal_word(word))

    def test1_same_length(self):
        first = 'lead'
        second = 'gold'
        self.assertTrue(legal_word(first, second))
    
    def test2_same_length(self):
        first = 'bird'
        second = 'goanna'
        self.assertFalse(legal_word(first, second))

class TestLegalDictionary(unittest.TestCase):
    


if __name__ == "__main__":
    unittest.main()