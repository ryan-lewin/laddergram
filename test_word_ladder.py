#!/usr/bin/env python

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

class TestBuild(unittest.TestCase):
    def test_pattern_1(self):
        self.assertEqual((build('like', ['like', 'tire', 'bird'], {}, [])), ['like'])

    def test_pattern_2(self):
        word = 'life'
        self.assertEqual((build(word[1], ['like', 'tire', 'bird'], {}, [])), ['like', 'tire', 'bird'])

    def test_pattern_2(self):
        word = 'life'
        self.assertEqual((build(word[3], ['like', 'tire', 'bird'], {}, [])), ['like', 'tire'])

    def test_in_seen(self):
        self.assertEqual((build('like', ['like', 'tire', 'bird'], {'like': 1}, [])), [])

    def test_in_list(self):
        self.assertEqual((build('tire', ['like', 'tire', 'bird'], {}, ['tire'])), [])

class TestReadDictionary(unittest.TestCase):
    def test_correct_count_1(self):
        self.assertEqual(len(read_dictionary('dictionary.txt', 'hi', [])), 94)

    def test_correct_count_2(self):
        self.assertEqual(len(read_dictionary('dictionary.txt', 'hi', ['bo', 'ag', 'to'])), 91)

    def test_excludes_words(self):
        words = read_dictionary('dictionary.txt', 'start', ['bear'])
        self.assertTrue('bear' not in words)

    def test_filter_word_lengths(self):
        start = 'test'
        words = read_dictionary('dictionary.txt', start, [])
        filtered = [False for word in words if len(word) != len(start)]
        self.assertTrue(False not in filtered)

class TestExistsAlongPath(unittest.TestCase):
    def no_path_exists(self):
        words = ['test', 'rest', 'flow', 'stop', 'neck']
        start = 'gold'
        pit_stop = 'hide'
        self.assertEqual(exists_along_path(start, words, {}, pit_stop, [], 'No path found'))

if __name__ == "__main__":
    unittest.main()