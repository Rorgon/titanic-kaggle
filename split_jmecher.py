import numpy as np
import pandas as pd

data = pd.read_csv('train.csv')
train=data.sample(frac=0.7)
test=data.drop(train.index)

train.to_csv('train2.csv',index=False)
test.to_csv('test2.csv',index=False)



