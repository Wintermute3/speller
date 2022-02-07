#!/usr/bin/env python3

# helps solve wordle.  enter 5-character word and wordle
# response (using =, + or -), and iterate.

import os

def PossibleMatch(Candidate, Guess, Response):
  for i in range(0,5):
    if Response[i] == '-': # not present in word
      if Guess[i] in Candidate:
        return False
    if Response[i] == '=': # present, in right place
      if Guess[i] == Candidate[i]:
        Guess[i] == ' ' # prevent cross-matching
      else:
        return False
    if Response[i] =='+': # present, in wrong place
      Match = False
      for j in range(0,5):
        if not Match:
          if Guess[i] == Candidate[j]:
            Guess[i] == ' ' # prevent cross-matching
            Match = True
      if not Match:
        return False
  return True

Candidates = []
with open('words.txt') as Words:
  for Word in Words:
    Word = Word.strip().lower()
    if len(Word) == 5:
      Candidates.append(Word)

while True:
  print()
  Guess    = input('   guess: ')
  Response = input('response: ')
  print()
  NextCandidates = []
  for Candidate in Candidates:
    if PossibleMatch(Candidate, Guess, Response):
      NextCandidates.append(Candidate)
      if len(NextCandidates) % 10 == 0:
        print()
      print('  %s' % (Candidate), end='')
  Candidates = NextCandidates
  print()
  if len(Candidates) < 2:
    break
  print()
