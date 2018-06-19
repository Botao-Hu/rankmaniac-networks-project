#!/usr/bin/env python

import sys
# import numpy as numpy
import heapq

#
# This program simply represents the identity function.
#
CPR_list = []
PPR_list = []
node_list = []
temp_line = []
for line in sys.stdin:
	s = line.split()
	nodeID = s[0]
	nodeID = nodeID.split(':')[1]
	ss = s[1].split(';')
	IT = int(ss[0])
	s1 = ss[1].split(',')
	CPR, PPR = float(s1[0]), float(s1[1])
	if IT >= 5:
		temp_CPR = CPR
		CPR = 1.1*CPR - 0.1*PPR
		PPR = temp_CPR
	CPR_list.append(CPR)
	PPR_list.append(PPR)
	node_list.append(nodeID)
	outlinks = ','.join(s1[2:])
	if len(outlinks) == 0:
		temp_line.append(s[0] + '\t' + str(IT) + ';' + str(CPR) + ',' + str(PPR) + '\n')
	else:
		temp_line.append(s[0] + '\t' + str(IT) + ';' + str(CPR) + ',' + str(PPR) + ',' + outlinks + '\n')
idx1 = heapq.nlargest(25, range(len(CPR_list)), CPR_list.__getitem__ )
idx2 = heapq.nlargest(25, range(len(PPR_list)), PPR_list.__getitem__ )
if idx1 == idx2 or IT == 50:
	for idx in idx1[:20]:
		line1 = 'FinalRank:' + str(CPR_list[idx]) + '\t' +  node_list[idx] +'\n'
		sys.stdout.write(line1)
else:
	for line in temp_line:
		sys.stdout.write(line)






