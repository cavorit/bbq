import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

print(movies.shape) # 979 rows

booleans = []
for length in movies.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)
print(booleans)
print(len(booleans))
print(sum(booleans))

film_is_long = pd.Series(booleans)
print(film_is_long.head())

print(movies[film_is_long]) # as axis=0 is default


#### and now more condesed

film_is_long = movies.duration >= 200
print(film_is_long.head())

movies[movies.duration >= 200].genre
# alternative:
movies.loc[movies.duration >= 200, 'genre'] # very like R







