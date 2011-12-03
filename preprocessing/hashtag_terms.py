#!/usr/bin/env python
import sys
from nltk.tokenize import WhitespaceTokenizer


def main(argv):
    # looping over input
    for line in sys.stdin:
        if line.find('\t') == -1:
            continue
        line = line.strip()
        date, user, post = line.split('\t', 2)
        
        tokens = WhitespaceTokenizer().tokenize(post)
        for i in range(len(tokens)):
            if tokens[i][0] == '#':
                for j in range(len(tokens)):
                    if i != j:
                        print "\t".join((tokens[i], tokens[j], date, user))
    
if __name__ == '__main__':
    main(sys.argv)