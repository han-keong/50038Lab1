#!/usr/bin/python

import sys

topFile = None
maxHits = 0
currentFile = None
numHits = 0

for line in sys.stdin:
    thisFile = line.strip()
    
    if currentFile and thisFile != currentFile:
        if numHits > maxHits:
            topFile = currentFile
            maxHits = numHits
        currentFile = thisFile
        numHits = 0
    
    currentFile = thisFile
    numHits += 1

if topFile:
    print "most popular file: " + topFile.rsplit("/", 1)[-1]
    print "number of occurences:", maxHits
