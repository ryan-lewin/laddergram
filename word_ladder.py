#!/usr/bin/env python

import re
import os

def match_letters(start_word, target):
  """
  Searches for matching letters between the search word and target. Returns a list with indexes of the
  matching letters.
  """
  matches = []
  for(start_word_i, target_i) in zip(start_word, target):
    if start_word_i == target_i:
      matches = [i for i, x in enumerate(zip(start_word, target)) if all(y == x[0] for y in x)]
  return matches

def same(item, target):
  """
  Returns the number of matching letters in the item and target
  """
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  """
  Returns a list of words from the read file that match the pattern against the target word and are not
  in the seen dict
  """
  return [word for word in words if re.search(pattern, word) and word not in seen.keys() and word not in list]

def find(word, words, seen, target, path):
  """
  Creates a list of possible words and loops over until target word is reached
  """
  list = []
  matching_letters = match_letters(word, target)

  for i in range(len(word)):
    if i not in matching_letters:
      list += build(word[:i] + "." + word[i + 1:], words, seen, list) #calls build with a list of patterns e.g. .ead, l.ad, le.d, lead. and feeds to build function
  if len(list) == 0:
    return False

  list = sorted([(same(w, target), w) for w in list], reverse=True) # updates list to include number of matching letters and sorts by number of matches
  
  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True

  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

def legal_word(word, words, start_word = None):
  """
  Validates word. Returns True if word is alpha and optionally if word lengths match.
  """
  if word not in words:
    return False
  elif start_word == None or len(start_word) == len(word):
    for i in word:
      if not i.isalpha():
        return False
  elif len(start_word) != len(word):
        return False
  return True

def legal_dictionary(f_name):
  """
  Validates the input of the dictionary file name. Returns True is dictionary exists and is a falid file, else False'
  """
  f_name_parts = f_name.split('.')
  if len(f_name_parts) != 2 or f_name_parts[1] != 'txt':
    return False
  elif not os.path.exists(f_name):
    return False
  return True

def excluded_words(words_string):
  return words_string.split()

def path_with_stop(start, words, seen, target, pit_stop, path):
  """
  Forces the input word to appear along the path.
  start -> pitStop -> target
  """
  if find(start, words, seen, pit_stop, path):     #start -> pitStop
    path.append(pit_stop)
  else:
    pit_stop = start
    print("No path found from start to target with mandatory word.")
  if find(pit_stop, words, seen, target, path):    #pitStop -> target
    path.append(target)
    print(len(path) - 1, path)                        
  else:
    print("No path found from start to target.")


def read_dictionary(fname, start = None, exclusions = None):
  file = open(fname)
  lines = file.readlines()
  words = []
  for line in lines:
    word = line.rstrip()
    if start != None:
      if len(word) == len(start) and word not in exclusions:
        words.append(word.upper())
    else:
      words.append(word.upper())
  return words

# while True:
#   words = []
#   while True:
#     fname = ('dictionary.txt')
#     if legal_dictionary(fname):
#       words = read_dictionary(fname)
#       break
#     print('Invalid Filename!')
#   while True:
#     start = input("Enter start word: ").strip().upper()
#     if legal_word(start, words):
#       break
#     print('Invalid Entry!')
#   while True:
#     target = input("Enter target word: ").strip().upper()
#     if legal_word(target, words):
#       break
#     print('Invalid Entry!')
#   exclusions = input('Enter words you wish to exclude separated by a space or press enter to skip: ')
#   pit_stop_required = input('Would you like to include a mandatory word along the path? [Enter Y for yes]: ').strip().upper()

#   words = read_dictionary(fname, start, exclusions)
#   path = [start]
#   seen = {start : True}
  
#   if pit_stop_required == 'Y':
#     while True:
#       pit_stop = input("Enter target word: ").strip().upper()
#       if legal_word(pit_stop, words, start):
#         break
#       print('Invalid Entry!')
#     path_with_stop(start, words, seen, target, pit_stop, path)
#   else:
#     if find(start, words, seen, target, path):    #pitStop -> target
#       path.append(target)
#       print(len(path) - 1, path)                        
#     else:
#       print("No path found from start to target.")
#   break
  