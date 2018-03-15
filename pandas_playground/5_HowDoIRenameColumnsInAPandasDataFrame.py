import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.head())

# rename columns really secure: 'Color Reported' in 'ColorReported'

print(ufo.columns)

ufo.rename(columns= {'Colors Reported':'Colors_Reported', 
    'Shape Reported':'Shape_Reported'}, # old:new
    inplace=True) # I think this is call by reference

print(ufo.columns) # r >>> colnames(ufo)

# alternativ (and maybe less secure)

x = ['city', 'colors', 'shape', 'state', 'time']
ufo.columns = x

# or 
ufo=pd.read_csv('https://bit.ly/uforeports', header=0, names=x)

# remove all white spaces with string methode

ufo.columns = ufo.columns.str.replace(' ', '_') # replace space by _




