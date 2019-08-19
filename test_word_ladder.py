import unittest
import os
from word_ladder import*

class TestLegalWord(unittest.TestCase):
    def test_all_alpha(self):
        word = 'hello'
        self.assertTrue(legal_word(word))

    def test_not_alpha(self):
        word = '$$hELLO999'
        self.assertFalse(legal_word(word))

    def test_if_numbers(self):
        word = '1234567'
        self.assertFalse(legal_word(word))

    def yesy_same_length(self):
        first = 'lead'
        second = 'gold'
        self.assertTrue(legal_word(first, second))
    
    def test_not_same_length(self):
        first = 'bird'
        second = 'goanna'
        self.assertFalse(legal_word(first, second))

class TestLegalDictionary(unittest.TestCase):
    def test_invalid_fname(self):
        fname = 'open.this.file.txt'
        self.assertFalse(legal_dictionary(fname))

    def test_valid_fname_exists(self):
        fname = 'this-is-a-valid-file.txt'
        test_file = open(fname, 'x')
        self.assertTrue(legal_dictionary(fname))
        os.remove(fname)

    def test_not_exists(self):
        fname = 'file.txt'
        self.assertFalse(legal_dictionary(fname))

    def test_exists(self):
        fname = 'testfile.txt'
        test_file = open(fname, 'x')
        self.assertTrue(legal_dictionary(fname))
        os.remove(fname)

class TestExcludedWords(unittest.TestCase):
    def test_correct_splitting(self):
        string = 'This is a test string'
        self.assertEqual(excluded_words(string), ['This', 'is', 'a', 'test', 'string'])

    def test_no_whitespace(self):
        string = 'so much       white      space in this      string'
        self.assertTrue(' ' not in excluded_words(string))

    def test_correct_length(self):
        string = 'This is a test string'
        length = 5
        self.assertEqual(len(excluded_words(string)), length)

class TestSame(unittest.TestCase):
    def test_one_match(self):
        first = 'bear'
        second = 'claw'
        self.assertEqual(same(first, second), 1)

    def test_all_match(self):
        first = 'same'
        second = 'same'
        self.assertEqual(same(first, second), 4)

    def test_all_match(self):
        first = 'none'
        second = '----'
        self.assertEqual(same(first, second), 0)

if __name__ == "__main__":
    unittest.main()