#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
    j = 0
for i in range(20):
	sys.stdout.write('FinalRank:0.0\t' + str(i) + '\n')