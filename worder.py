#!/usr/bin/env python3

#---------------------------------------------------------
# helps solve wordle.  enter 5-character word and wordle
# response (using =, + or -), and iterate.
#---------------------------------------------------------

Interactive = True

#---------------------------------------------------------
# sequence of test guesses and responses
#---------------------------------------------------------

if not Interactive:
  TestList = [
    {'guess': 'laser', 'response': '-+-++'},
    {'guess': 'arena', 'response': '+=+--'},
    {'guess': 'erode', 'response': '-=--='},
    {'guess': 'erred', 'response': '+=---'},
    {'guess': 'crate', 'response': '-==-='},
    {'guess': 'frame', 'response': '====='},
  ]

#---------------------------------------------------------
# evaluate a candidate against a guess using the response
# template
#---------------------------------------------------------

def PossibleMatch(Candidate, Guess, Response):
  Guess = list(Guess)
  Candidate = list(Candidate)
  for i in range(0,5):
    if Response[i] == '=': # present, in right place
      if Guess[i] == Candidate[i]:
        Guess[i] = ' ' # prevent cross-matching
        Candidate[i] = ' ' # prevent cross-matching
      else:
        return False
  for i in range(0,5):
    if Response[i] =='+': # present, in wrong place
      Match = False
      for j in range(0,5):
        if i != j:
          if Guess[i] == Candidate[j]:
            Guess[i] = ' ' # prevent cross-matching
            Candidate[j] = ' ' # prevent cross-matching
            Match = True
      if not Match:
        return False
  for i in range(0,5):
    if Response[i] == '-': # not present in word
      if Guess[i] in Candidate:
        return False
  return True

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
# play the game, either interactively or using a canned
# set of guesses and responses for testing
#---------------------------------------------------------

if Interactive:
  while True:
    print()
    Guess    = input('   guess: ')
    Response = input('response: ')
    NextCandidates = []
    for Candidate in Candidates:
      if PossibleMatch(Candidate, Guess, Response):
        NextCandidates.append(Candidate)
    for i, Candidate in enumerate(NextCandidates):
      if i % 10 == 0:
        print()
      print('  %s' % (Candidate), end='')
    Candidates = NextCandidates
    print()
    if len(Candidates) < 2:
      break
else:
  for Test in TestList:
    Guess = Test['guess']
    Response = Test['response']
    print()
    print('   guess: %s' % (Guess))
    print('response: %s' % (Response))
    NextCandidates = []
    for Candidate in Candidates:
      if PossibleMatch(Candidate, Guess, Response):
        NextCandidates.append(Candidate)
    for i, Candidate in enumerate(NextCandidates):
      if i % 10 == 0:
        print()
      print('  %s' % (Candidate), end='')
    Candidates = NextCandidates
    print()
    if len(Candidates) < 2:
      break
print()

#---------------------------------------------------------
# end
#---------------------------------------------------------
