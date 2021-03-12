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
  if len(arg) == 1:
    Letters.append(arg.upper())
  else:
    for Letter in arg:
      Letters.append(Letter.upper())

print('%s' % (Letters))

with open('words.txt') as Words:
  for Word in Words:
    Word = Word.strip()
    AllLettersMatch = True
    CenterLetterMatch = False
    for Letter in Word:
      if Letter == Letters[0]:
        CenterLetterMatch = True
      if not Letter in Letters:
        AllLettersMatch = False
        next
    if AllLettersMatch and CenterLetterMatch:
      if len(Word) > 3:
        MatchCount = 0
        for Letter in Letters:
          if Letter in Word:
            MatchCount += 1
        if MatchCount == 7:
          print('*** %s' % (Word))
        else:
          print('    %s' % (Word))
