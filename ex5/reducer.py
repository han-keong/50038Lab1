#!/usr/bin/python

import sys

currentFile = None
numHits = 0

for line in sys.stdin:
    thisFile = line.strip()
    
    if currentFile and thisFile != currentFile:
        print currentFile, "\t", numHits
        currentFile = thisFile
        numHits = 0
    
    currentFile = thisFile
    numHits += 1

if currentFile:
    print currentFile, "\t", numHits
