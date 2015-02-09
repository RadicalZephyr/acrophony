#!/bin/env python
from __future__ import print_function
import sys


acrophones = {'a' : 'alpha',
	      'b' : 'bravo',
	      'c' : 'charlie',
	      'd' : 'delta',
	      'e' : 'echo',
	      'f' : 'foxtrot',
	      'g' : 'golf',
	      'h' : 'hotel',
	      'i' : 'india',
	      'j' : 'juliet',
	      'k' : 'kilo',
	      'l' : 'lima',
	      'm' : 'mike',
	      'n' : 'november',
	      'o' : 'oscar',
	      'p' : 'papa',
	      'q' : 'quebec',
	      'r' : 'romeo',
	      's' : 'sierra',
	      't' : 'tango',
	      'u' : 'uniform',
	      'v' : 'victor',
	      'w' : 'whiskey',
	      'x' : 'xray',
	      'y' : 'yankee',
	      'z' : 'zulu'}

def acrophonify(string):
    [acrophones[ltr] for ltr in string if acrophones.has_key(ltr)]

def main():
    string = sys.stdin.readline().lower()
    print(" ".join(acrophonify(string)))
    
if __name__ == "__main__":
    main()
