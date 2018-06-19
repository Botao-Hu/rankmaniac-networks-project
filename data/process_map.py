#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
# 	s  = line.split()
# 	s1 = s[1].split(',')
# 	nodeIDPart = s[0].split(':')
# 	nodeID = nodeIDPart[1]
# 	CPR = float(s1[0])
# 	line = 'CPR' + '\t' + str(CPR) + ':' + nodeID + '\n'
    sys.stdout.write(line)

