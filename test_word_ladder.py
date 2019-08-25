#!/usr/bin/env python

import unittest
import os
from word_ladder import*

class TestLegalWord(unittest.TestCase):
    def test_all_alpha(self):
        words = ['like', 'tire', 'bird', 'hire']
        word = 'hire'
        self.assertTrue(legal_word(word, words))

    def test_not_alpha(self):
        words = ['like', 'tire', 'bird', '$$hELLO999']
        word = '$$hELLO999'
        self.assertFalse(legal_word(word, words))

    def test_if_numbers(self):
        words = ['like', 'tire', 'bird', 'hello']
        word = '1234567'
        self.assertFalse(legal_word(word, words))

    def test_same_length(self):
        words = ['like', 'tire', 'bird', 'lead', 'gold']
        first = 'lead'
        second = 'gold'
        self.assertTrue(legal_word(first, words, second))
    
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

class TestMatchLetters(unittest.TestCase):
    def test_one_matching_letter(self):
        first = 'lead'
        second = 'gold'
        self.assertEqual(match_letters(first, second), [3])

    def test_all_matching_letters(self):
        first = 'gold'
        second = 'gold'
        self.assertEqual(match_letters(first, second), [0, 1, 2, 3])

    def test_no_matching_letters(self):
        first = 'gold'
        second = 'tame'
        self.assertEqual(match_letters(first, second), [])

class TestSame(unittest.TestCase):
    def test_one_match(self):
        first = 'bear'
        second = 'claw'
        self.assertEqual(same(first, second), 1)

    def test_all_match(self):
        first = 'same'
        second = 'same'
        self.assertEqual(same(first, second), 4)

    def test_none_match(self):
        first = 'none'
        second = '----'
        self.assertEqual(same(first, second), 0)

class TestBuild(unittest.TestCase):
    def test_pattern_1(self):
        self.assertEqual((build('like', ['like', 'tire', 'bird'], {}, [])), ['like'])

    def test_pattern_2(self):
        word = 'life'
        self.assertEqual((build(word[1], ['like', 'tire', 'bird'], {}, [])), ['like', 'tire', 'bird'])

    def test_pattern_3(self):
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

class TestPathWithStop(unittest.TestCase):
    def test_path_found(self):
        start = 'LEAD'
        words = ['LEAD', 'READ', 'REAM', 'TEAM', 'TRAM', 'GRAM', 'GRAD', 'GOAD', 'GOLD']
        seen = {start : True}
        target = 'GOLD'
        pit_stop = 'GRAM'
        path = [start]
        path_with_stop(start, words, seen, target, pit_stop, path)
        self.assertEqual(path, words)

    def test_no_path_found(self):
        start = 'LEAD'
        words = ['LEAD', 'READ', 'REAM', 'TEAM', 'GRAM', 'GRAD', 'GOAD', 'GOLD']
        seen = {start : True}
        target = 'GOLD'
        pit_stop = 'GRAM'
        path = [start]
        path_with_stop(start, words, seen, target, pit_stop, path)
        self.assertNotEqual(path, words)

class TestFind(unittest.TestCase):
    def test_path_found(self):
        start = 'HIDE'
        words = ['HIDE', 'SIDE', 'SITE', 'SITS', 'SIES', 'SEES', 'SEEK']
        seen = {start : True}
        target = 'SEEK'
        path = [start]
        if find(start, words, seen, target, path):    #pitStop -> target
            path.append(target)
        else:
            path = 'No path found from start to target.'
        self.assertEqual(path, words)

    def test_no_path_found(self):
        start = ''
        words = ['HIDE', 'SIDE', 'SITE', 'SITS', 'SEEK']
        seen = {start : True}
        target = 'SEEK'
        path = [start]
        if find(start, words, seen, target, path):    #pitStop -> target
            path.append(target)
        else:
            path = 'No path found from start to target.'
        self.assertEqual(path, 'No path found from start to target.')

if __name__ == "__main__":
    unittest.main()