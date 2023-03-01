#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        print ('%s\t%s' % (word, 1))
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py