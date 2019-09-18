import pandas as pd

train = pd.read_csv('test2.csv')

def calculate(row):
    score=0
    if row['Pclass']==1:
        score=9
    elif row['Pclass']==2:
        score=6
    if row['Age']<=5:
        score= score+10
    elif row['Age']<=16:
        score= score+7
    elif row['Age']<=40:
        score= score+5
    if row['Sex']=='female':
        score=score+11
    return score

def check(row):
    return row['Score']>11


train['Score']= train.apply(lambda row: calculate(row), axis=1)

print('all:', train['Score'].mean())
print('survived:', train[train.Survived==1]['Score'].mean())
print('died:', train[train.Survived==0]['Score'].mean())

train['Predicted']= train.apply(lambda row: row['Score']>11, axis=1)
print('predicted:', train['Predicted'].mean())

train.to_csv('predicted2.csv',index=False)

