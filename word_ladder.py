"""
Code currently returns every possible word between the start and target words. 
leade to gold -> path == 481 | goal path == 3
"""

import re

# def find_matches(start, target):
#   """
#   Returns a list of bools indicating whether each index in start and target matches
#   """
#   letters = []
#   for count, letter in enumerate(zip(start, target)):
#     if(letter[0] == letter[1]):
#       letters.append(True)
#     else:
#       letters.append(False)
#   return letters

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
  matchedletters = []

  if (sum(1 for (c, t) in zip(word, target) if c == t)) > 0:
    matchedletters = [i for i, x in enumerate(zip(word, target)) if all(y == x[0] for y in x)]
 
  for i in range(len(word)):
    if i not in matchedletters:
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

# fname = input("Enter dictionary name: ")
fname = 'dictionary.txt'
file = open(fname)
lines = file.readlines()
while True:
  start = input("Enter start word:")
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)
  target = input("Enter target word:")
  break

count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

