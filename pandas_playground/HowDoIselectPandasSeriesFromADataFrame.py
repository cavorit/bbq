import pandas as pd

ufo = pd.read_table('http://bit.ly/uforeports', sep=',')
ufo = pd.read_csv('http://bit.ly/uforeports') # default: sep = ,

print(type(ufo)) # pandas.core.frame.DataFrame
print(ufo.head())

print(ufo['City'])
print(type(ufo['City'])) # pandas.core.series.Series

print(ufo.City) # dotnotation works not with whitespace character
# also it works not when 'City' was a method of data.frame

# creating new series in dataframe

ufo['V1'] =(ufo.City +' liegt in '  +ufo.State ) # Zuweisung geht nur über bracket-notation 

print(ufo.head())


