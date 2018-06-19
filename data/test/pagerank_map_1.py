#!/usr/bin/env python

import sys
import numpy as np

# This is a line split function
# input: line from sys.stdin
# output: 	[float] CPR, PPR
#			[int] nodeID
#			[list of int] outLinks
def lineSplit(line):
	s = line.split("\t")
	nodeIDPart = s[0].split(":")
	nodeID = int(nodeIDPart[1]) # change to str
	s1 = s[1].split(",")
	CPR = float(s1[0])
	PPR = float(s1[1])
	outLinks = [int(x) for x in s1[2:]]
	return nodeID, CPR, PPR, outLinks

# This is the mapper function
def Mapper(key, listOfValues):
	CPR = listOfValues[0]
	PPR = listOfValues[1]
	outLinks = listOfValues[2:]
	L = len(outLinks)
	links = '~' + str(CPR) + ',' + str(PPR)
	for x in outLinks:
		contribution = '%d\t%f\n' % (x, CPR / L)
		sys.stdout.write(contribution)
		links = links + ',' + str(int(x))
	outputLinks = '%d\t%s\n' % (key, links)
	sys.stdout.write(outputLinks)

# This is the main function
for line in sys.stdin:
    nodeID, CPR, PPR, outLinks = lineSplit(line)
    listOfValues = np.zeros(len(outLinks) + 2)
    listOfValues[0] = CPR
    listOfValues[1] = PPR
    listOfValues[2:] = outLinks
    Mapper(nodeID, listOfValues)
