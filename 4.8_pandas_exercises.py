import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
#(cars.cty > cars.hwy).any()
#mpg_df.cty > mpg_df.hwy.sum()
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
# TODO: this

print('#3 --------------------------------------------------')

mammals_df = data('Mammals') # load the dataset and store it in a variable
data('mammals', show_doc=True) # view the documentation for the dataset

# How many rows and columns are there?
print(mammals_df.shape)

# What are the data types?
print(mammals_df.info())

# What is print(mpg_df.nlargest(1, 'avg_mpg'))the the weight of the fastest animal?
print(mammals_df.nlargest(1, 'speed'))

# What is the overall percentage of specials?
print(mammals_df.specials.sum()/mammals_df.specials.count()*100)


# How many animals are hoppers that are above the median speed? What percentage is this?
number_hopppers = mammals_df[mammals_df.speed > (mammals_df.speed.median())]
print(mammals_df.hoppers.sum()/mammals_df.hoppers.count()*100)

print('=====<')

hoppers = mammals_df[mammals_df.hoppers]
median_speed = mammals_df.speed.median()

n_hoppers = hoppers[hoppers.speed > median_speed].shape[0]

percent_hoppers = n_hoppers / mammals_df.shape[0]

print(percent_hoppers)

print('=====>')


print('#4 --------------------------------------------------')

# Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.
def get_db_url(db, user, host, password):
    from sqlalchemy import create_engine
    url = f'mysql+pymysql://{user}:{password}@{host}/employees'
    return create_engine(url)


# Use your function to obtain a connection to the employees database.
from env import user, host, password
conn = get_db_url('employees', user, host, password)


# Read the employees and titles tables into two separate data frames
employees_df = pd.read_sql('SELECT * FROM employees;', conn)
titles_df = pd.read_sql('SELECT * FROM titles;', conn)

# Visualize the number of employees with each title.
# num_of_employee_df = pd.read_sql('SELECT title, COUNT(emp_no) FROM titles GROUP BY title;', conn, index_col='title')
# num_of_employee_df.plot.bar(rot=45)
# plt.show()
# titles_df.groupby('title').count()
# titles_df.value_counts()
# titles_df.title.value_counts()
# titles_df.title.value_counts().plot()
# titles_df.title.value_counts().plot.bar()
# plt.xticks(rotation=30)
# plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.2)
# titles.dtypes
# titles.to_date > 3
# titles.to_date != '9999-01-01'
# (titles.to_date != '9999-01-01').all()
# titles.to_date
# (titles.to_date != '9999-01-01').all()
# from datetime import datetime
# datetime.now()
# (titles.to_date > datetime.now()).any()
# (titles.to_date > datetime.date()).any()
# (titles.to_date > datetime.now().date).any()
# (titles.to_date > datetime.now().date()).any()
# titles.to_date > datetime.now().date()
# titles[titles.to_date > datetime.now().date()]
# current_titles = titles[titles.to_date > datetime.now().date()]
# current_titles.value_counts().plot.bar()
# current_titles.title.value_counts().plot.bar()
# current_titles.title.value_counts().plot.bar()


# Visualize how frequently employees change titles.
# titles.emp_no.value_counts()
# titles.emp_no.value_counts().value_counts()
# titles.emp_no.value_counts().value_counts().plot.bar()

# Use the .join method to join the employees and titles data frames together
# get_ipython().run_line_magic('pinfo', 'employees.join')
# employees.join(titles, on='emp_no')
# employees.join(titles, on='emp_no', lsuffix='_emp')
# employees.join(titles, on='emp_no', lsuffix='_emp', how='right')
# employees.join(titles, on='emp_no', lsuffix='_emp', how='inner')
# employees_with_titles = employees.join(titles, on='emp_no', lsuffix='_emp', how='inner')
# get_ipython().run_line_magic('pinfo', 'employees.merge')
# get_ipython().run_line_magic('pinfo', 'employees.join')


# For each title, find the hire date of the employee that was hired most recently with that title.
# employees_with_titles
# employees_with_titles.groupby('title')[['hire_date']].max()


# chipotle

url = get_db_url(env.username, env.hostname, env.password, db='chipotle')
connection = create_engine(url)
orders = pd.read_sql('SELECT * FROM orders')
orders = pd.read_sql('SELECT * FROM orders', connection)
orders.head()
orders.head()
orders.dtypes
orders.item_price.replace('')
orders.item_price.replace('$', '')
orders.item_price.str.replace('$', '')
orders.item_price.str.replace('$', '').astype('float')
orders.item_price = orders.item_price.str.replace('$', '').astype('float')
orders.head()
orders[orders.quantity >= 2]
orders[orders.quantity >= 2].head(20)
orders[orders.quantity >= 2].head(20).drop(columns=['choice_description', 'id', 'order_id'])
orders[orders.item_name == 'Canned Soda']
orders[orders.item_name == 'Canned Soda'].choice_description
orders[orders.item_name == 'Canned Soda'].choice_description.value_counts()
orders.groupby('order_id').sum()
orders[['order_id', 'item_price']].groupby('order_id').sum()
order_prices = orders[['order_id', 'item_price']].groupby('order_id').sum()
order_prices.plot.hist()
order_prices.describe()
orders.item_name.value_counts()
orders.item_name.value_counts().head(7)
orders[['item_name', 'item_price']].groupby('item_name').sum()
orders[['item_name', 'item_price']].groupby('item_name').sum().sort_values('item_price')
orders[['item_name', 'item_price']].groupby('item_name').sum().nlargest(7)
orders[['item_name', 'item_price']].groupby('item_name').sum().nlargest(7, 'item_price')
orders.item_name.value_counts().head(7)

