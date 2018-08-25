#!/usr/bin/env python3

import sys
import os

arguments = sys.argv

counter = 0

if len(arguments) == 3:
	searchPath = arguments[1]
	extension = arguments[2]
	if os.path.isdir(searchPath):
		for curDir,subDirs,subFiles in os.walk(searchPath):
			for subFile in subFiles:
				absPath = os.path.join(curDir,subFile)
				if absPath.endswith(extension):
					print( ': {}'.format(absPath) )
					counter = counter + 1
		print('Total : {}'.format(counter))   
	else:
		print('')
		print('Directory {} not found'.format(searchPath))
		print('')

else:
	print('')
	print('Usage : filefinder  Path Extension')
	print('')
