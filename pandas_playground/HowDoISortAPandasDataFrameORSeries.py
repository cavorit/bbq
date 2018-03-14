import pandas as pd
ufo = pd.read_csv('http://bit.ly/uforeports')

print(ufo.shape)
print(ufo.head())

######### SORT_VALUE is the new way

print(ufo.Time.sort_values(ascending=True)) 
# only sorts the series and returns a series
# so it is a series mehtod 
# it is not inplace

# now lets sort whole DF 
x = ufo.sort_values('Time') 
print(x)

################ now sorting by several columns

movies = pd.read_csv('http://bit.ly/imdbratings')
print(movies.head())

print(movies.sort_values(['content_rating', 'duration']))


