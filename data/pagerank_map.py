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
	ss = s[1].split(";")
	if len(ss) == 1:
		IT = 1
	else:
		IT = int(ss[0]) + 1
	s1 = ss[-1].split(",")
	CPR = float(s1[0])
	PPR = float(s1[1])
	outLinks = [int(x) for x in s1[2:]]
	return nodeID, IT, CPR, PPR, outLinks

# This is the mapper function
def Mapper(key, listOfValues):
	alpha = 0.85
	IT = listOfValues[0]
	CPR = listOfValues[1]
	PPR = listOfValues[2]
	outLinks = listOfValues[3:]
	L = len(outLinks)
	links = '~' + str(int(IT)) + ';' + str(CPR) + ',' + str(PPR)
	if L == 0:
		contribution = '%d\t%f\n' % (key, CPR * alpha)
		sys.stdout.write(contribution)
	for x in outLinks:
		contribution = '%d\t%f\n' % (x, CPR / L * alpha)
		sys.stdout.write(contribution)
		links = links + ',' + str(int(x))
	outputLinks = '%d\t%s\n' % (key, links)
	sys.stdout.write(outputLinks)

# This is the main function
for line in sys.stdin:
    nodeID, IT, CPR, PPR, outLinks = lineSplit(line)
    listOfValues = np.zeros(len(outLinks) + 3)
    listOfValues[0] = IT
    listOfValues[1] = CPR
    listOfValues[2] = PPR
    listOfValues[3:] = outLinks
    Mapper(nodeID, listOfValues)
