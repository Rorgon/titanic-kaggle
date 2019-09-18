import numpy as np
import pandas as pd
import random

file = open('train.csv','r')
train = open('train0.csv','w+')
test = open('test0.csv','w+')
lineList = file.readlines()
header=lineList[0]
lines=lineList[1:]
train.write(header)
test.write(header)
random.shuffle(lines)

percentage = 0.3

for i in range(len(lines)):
    if i<(percentage*len(lines)):
        test.write(lines[i])
    else:
        train.write(lines[i])

