#!/usr/bin/env python3

# solves nyt spelling bee, enter center letter first,
# then the other letters, for example like this:
#
#        ./speller.py n o i h t d a
#
# for this arrangement:
#
#             I
#         O       H
#             N
#         T       D
#             A
#
# program will emit a list of candidate words culled
# from the collins scrabble words 2019 list.  lowercase
# is acceptable for entry.

import sys

Letters = []
for arg in sys.argv[1:]:
  Letters.append(arg.upper())

print('%s' % (Letters))

with open('words.txt') as Words:
  for Word in Words:
    Word = Word.strip()
    Match1 = True
    Match2 = False
    for Letter in Word:
      if Letter == Letters[0]:
        Match2 = True
      if not Letter in Letters:
        Match1 = False
        next
    if Match1 and Match2:
      print('%s' % (Word))
