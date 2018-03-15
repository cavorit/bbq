import pandas as pd

# assuming by default header and tab separation
orders = pd.read_table('http://bit.ly/chiporders')
print(orders.head())


user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code' ]
X = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)

print(X.head())



