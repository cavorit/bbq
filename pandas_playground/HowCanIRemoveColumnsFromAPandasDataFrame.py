import pandas as pd
x = pd.read_csv('http://bit.ly/uforeports')
print(x.head())
print(x.shape)

# get rid of one column

x.drop('Colors Reported', axis=1, inplace=True) # axes=0 is row
# inplace = True --> call by reference

x.drop(['City', 'State'], axis=1, inplace=True)

print(x.head())

# now let's drop the first two observations

x.drop([0, 1], axis=0, inplace=True) 

