import pandas as pd
test = pd.read_csv('test2.csv')
train = pd.read_csv('train2.csv')

females = train[train.Sex == 'female']['Survived']
males = train[train.Sex == 'male']['Survived']
first = train[train.Pclass == 1]['Survived']
second = train[train.Pclass == 2]['Survived']
third = train[train.Pclass == 3]['Survived']
firstAndFemale = train[train.Sex == 'female'][train.Pclass == 1]['Survived']
babies = train[train.Age < 8]['Survived']
teens = train[train.Age >= 8][train.Age <= 15]['Survived']
adults = train[train.Age > 15][train.Age < 60]['Survived']
oldies = train[train.Age >60]['Survived']

print('all:', train['Survived'].mean())
print('male:', males.mean())
print('female:', females.mean())
print('1st:', first.mean())
print('2nd:', second.mean())
print('3rd:', third.mean())
print('1st and female:', firstAndFemale.mean())
print('babies:', babies.mean())
print('teens:', teens.mean())
print('adults:', adults.mean())
print('oldies:', oldies.mean())

