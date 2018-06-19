#!/usr/bin/env python

import sys
import collections
#
# This program simply represents the identity function.
#
def reducer(key, listOfValues):
	sumOfValues = 0
	for value in listOfValues:
		if value[0] != '~':
			sumOfValues += float(value)
		else:
			line = value[1:]
	line = line.split(',')
	line[1] = line[0]
	line[0] = str(sumOfValues)
	line = ','.join(line)
	line = 'NodeId:' + key + '\t' + line
	sys.stdout.write(line)

# data = collections.defaultdict(list)
for line in sys.stdin:
	sys.stdout.write(line)
# 	key, value = line.split()
# 	data[key].append(value)
# for key in data:
# 	listOfValues = data[key]
# 	reducer(key, listOfValues)

