#!/usr/bin/env python3

#---------------------------------------------------------
# find the longest sets of 5-letter words that differ in
# a single letter
#---------------------------------------------------------

#---------------------------------------------------------
# load the word list, filtered to 5-character words
#---------------------------------------------------------

Candidates = []
with open('words.txt') as Words:
  for Word in Words:
    Word = Word.strip().lower()
    if len(Word) == 5:
      Candidates.append(Word)

#---------------------------------------------------------
# return true if x and y differ only in position n
#---------------------------------------------------------

def Diff1(x, y, n):
  for i in range(0,5):
    if i != n:
      if x[i] != y[i]:
        return False
  return True

#---------------------------------------------------------
#
#---------------------------------------------------------

Sets = []
Longs = {}
Count = len(Candidates)
for n in range(0, 5):
  Sets.append({})
  for i in range(0, Count):
    Word1 = Candidates[i]
    for j in range(i+1, Count):
      Word2 = Candidates[j]
      if Diff1(Word1, Word2, n):
        if not Word1 in Sets[n]:
          Sets[n][Word1] = [Word1]
        Sets[n][Word1].append(Word2)
        if not Word1 in Longs:
          Longs[Word1] = Sets[n][Word1]
for Long in sorted(Longs):
  if len(Longs[Long]) > 10:
    print('%2d %s' % (len(Longs[Long]), Longs[Long]))

#---------------------------------------------------------
# end
#---------------------------------------------------------
