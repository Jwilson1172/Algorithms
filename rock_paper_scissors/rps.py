#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  moves = ['rock', 'paper', 'scissors']
  # for n = 1
  # ouptut = ['rock', 'paper', 'scissors']
  # for n = 2
  # output = [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'],
  # ['paper', 'rock'], ['paper', 'paper'],['paper', 'scissors'], ['scissors',
  # 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
  pass


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
