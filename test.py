import pandas as pd

train= pd.read_csv('predicted2.csv')

print('accuracy:', len(train[train.Predicted==train.Survived])/len(train))
