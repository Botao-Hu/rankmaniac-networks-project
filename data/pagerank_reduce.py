#!/usr/bin/env python

import sys
import collections
#
# This program simply represents the identity function.
#

def reducer(key, listOfValues):
	alpha = 0.85
	sumOfValues = 1 - alpha
	for value in listOfValues:
		if value[0] != '~':
			sumOfValues += float(value)
		else:
			line = value[1:]
	temp = line.split(';')
	line = temp[1].split(',')
	line[1] = line[0]
	line[0] = str(sumOfValues)
	line = ','.join(line)
	line = 'NodeId:' + key + '\t' + temp[0] + ';' + line +'\n'
	sys.stdout.write(line)

data = collections.defaultdict(list)
for line in sys.stdin:
	key, value = line.split()
	data[key].append(value)
for key in data:
	listOfValues = data[key]
	reducer(key, listOfValues)

