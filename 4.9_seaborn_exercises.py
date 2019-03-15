import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


iris = sns.load_dataset('iris')

print(iris.dtypes)

# What does the distribution of petal lengths look like?
sns.distplot(iris.petal_length)
plt.show()

# Is there a correlation between petal length and petal width?
print(iris[['petal_length', 'petal_width']].corr())

# Would it be reasonable to predict species based on sepal width and sepal length?
print(iris[['sepal_length', 'sepal_width']].corr())
sns.relplot(x='sepal_width', y='sepal_length', data=iris, style="species")
sns.relplot(x='petal_width', y='petal_length', data=iris, style="species")
plt.show()

# Which features would be best used to predict species?
print('petal_width and petal_length')

# 1. Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set.
# Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset.
# What do you notice?
anscombe = sns.load_dataset('anscombe')
print(anscombe.dtypes)
x = pd.anscombe[['x', 'y']]

# x.describe()
# y.describe()

# - Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

# 2. Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows the
# effectiveness of the different insect sprays.

# 3. Load the swiss dataset and read it's documentation. Create visualizations to
# answer the following questions:

# - Create a column named is_catholic that holds a boolean value of whether or not the province is
# 	Catholic. (Choose a cutoff point for what constitutes catholic)

# - Does whether or not a province is Catholic influence fertility?

# - What measure correlates most strongly with fertility?

# 4. Using the chipotle dataset from the previous exercise, create a barplot that shows the 4
# most popular items and the revenue produced by each.

# Load the sleepstudy data and read it's documentation. Use seaborn to create a line plot ofall the
# individual subject's reaction times and a more prominant line showing the average change in reaction time.





