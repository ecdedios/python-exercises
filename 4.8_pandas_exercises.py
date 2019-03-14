import numpy as np
import pandas as pd

print('#1 --------------------------------------------------')

numerics = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
  
# Calling DataFrame constructor on list 
numerics_df = pd.DataFrame(numerics)

numerics_df[0] = numerics_df[0].str.strip('$')
numerics_df[0] = numerics_df[0].str.replace(',','')
numerics_df[0] = numerics_df[0].astype(float)
print(numerics_df[0])



print('#2 --------------------------------------------------')

from pydataset import data

mpg_df = data('mpg') # load the dataset and store it in a variable
data('mpg', show_doc=True) # view the documentation for the dataset

# How many rows and columns are there?
print(mpg_df.shape)

# What are the data types?
print(mpg_df.info())


# Do any cars have better city mileage than highway mileage?
# NO
better_city = mpg_df[mpg_df.cty > mpg_df.hwy]
print(better_city)

# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
mpg_df['difference'] = (mpg_df.hwy - mpg_df.cty)
print(mpg_df)

# On average, which manufacturer has the best miles per gallon?
mpg_df['avg_mpg'] = (mpg_df.cty + mpg_df.hwy) / 2
print(mpg_df.nlargest(1, 'avg_mpg'))

# How many different manufacturers are there?
# 15
print(mpg_df.nunique())


# How many different models are there?
# 38
print(mpg_df.nunique())



# Do automatic or manual cars have better miles per gallon?


print('#3 --------------------------------------------------')

mammals_df = data('Mammals') # load the dataset and store it in a variable
data('mammals', show_doc=True) # view the documentation for the dataset

# How many rows and columns are there?
print(mammals_df.shape)

# What are the data types?
print(mammals_df.info())

# What is print(mpg_df.nlargest(1, 'avg_mpg'))the the weight of the fastest animal?
print(mammals_df.nlargest(1, 'speed'))

# What is the overal percentage of specials?
print(mammals_df.specials.sum())

# How many animals are hoppers that are above the median speed? What percentage is this?
number_hopppers = mammals_df[mammals_df.speed > (mammals_df.speed.median())]
print(mammals_df.hoppers.sum()/mammals_df.hoppers.count()*100)



print('#4 --------------------------------------------------')














