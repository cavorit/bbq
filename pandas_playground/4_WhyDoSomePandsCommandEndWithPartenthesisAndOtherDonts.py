import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
print(movies.head())

print(movies.describe()) # r>>> summary_statistics

print(movies.shape)
print(movies.dtypes) # r >>> structure >>> str(

print(movies.describe(include=['object']) # weniger quantitative stats


        

