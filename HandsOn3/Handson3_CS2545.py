#!/usr/bin/env python
# coding: utf-8

# # Hands-on 3
# 
# ### CS2545 - Data Science ###
# ### Winter, 2023 ###
# ### UNB, Fredericton ###
# 
# Please complete the following and submit this notebook (filename: handson3-**lastname**-**firstname**.ipynb) on D2L by **11:59pm, Friday, February 24**. 
# </br>
# Late submission until **11:59pm, Sunday, February 26 is possible** with a **penalty of 5%**. 
# </br>
# </br>

# **Q1.**  Create a 7X7 NumPy array with random numbers. Print the element at 2nd row, 3rd column and the element at 5th row and 6th column. **(2 points)**

# In[15]:


import numpy as np
import random

#seed=np.random.seed(987654)
x=np.random.random(49)

#arr= np.arange(x)
arr2= x.reshape(7,7)
print(arr2[1,2])
print(arr2[5,6])
# your code should start here


# **Q2.a** In the following, the list *closing_price* contains historical stock prices (closing price) of a technology company listed with NYSE. The *dates* list contains the corresponding dates.
# 
# Using list comprehension create a list *range_prices*, which contains stock prices (closing price) that are between 120 and 130. **(3 points)**
# 
# 
# **Q2.b** Create a Pandas data series  *stock_data_series* from the list *closing_price* (as values) and *dates* (as index). Then, using a NumPy function find the median and average stock price. **(3 points)**

# In[32]:


import numpy as np
import pandas as pd

closing_price = [139.02, 140.85, 141.13, 145.11, 134.05, 130.55, 129.10, 130.02, 131.21, 127.20, 126.45, 124.79, 119.64, 115.40, 115.43, 116.83, 115.67, 120.06, 123.12, 124.84, 123.38, 123.54]

dates = ['10/11/2023', '10/12/2023', '10/15/2023', '10/16/2023', '10/17/2023', '10/18/2023', '10/19/2023', '10/22/2023', '10/23/2023', '10/24/2023', '10/25/2023', '10/26/2023', '10/29/2023', '10/30/2023',  '10/31/2023', '11/1/2023', '11/2/2023', '11/5/2023', '11/6/2023', '11/7/2023', '11/8/2023', '11/9/2023']

# Q2.a

range_prices= [x for x in closing_price if x>120 and x<130 ]
print(range_prices)

# Q2.b

s = pd.Series(closing_price,dates)
print(s)
mean=np.mean(closing_price)
median=np.median(closing_price)

print("Mean: ")
print(mean)
print("Median: ")
print(median)


# **Q3.**  Download the *cereal.csv* file from Hands-on 2. This includes information about the per serving nutritional content of a number of breakfast cereals. The columns in this file represent the following fields (detail and short) and data types: <br>
# cereal name [name] - String <br>
# manufacturer [mfr] - String <br>
# type (cold/hot) [type] - String  <br>
# calories (number) [calories] - Int <br>
# protein(g) [protein] - Int <br>
# fat(g) [fat] - Int <br>
# sodium(mg) [sodium] - Int <br>
# dietary fiber(g) [fiber] - Float <br>
# complex carbohydrates(g) [carbo] - Float <br>
# sugars(g) [sugars] -  Int <br>
# display shelf (1, 2, or 3, counting from the floor) [shelf] - Int <br>
# potassium(mg) [potass] - Int <br>
# vitamins & minerals  [vitamins] - Int <br>
# weight (in ounces) of one serving (single serving size) [weight] - Float <br>
# cups per serving [cups] - Float <br>
# rating - Float <br>
# <br>
# 
# Note, the value -1 indicates missing data.
# 
# 
# **Q3.a** Load the data file *cereal.csv* into a dataframe *cereal_df* and show the first 7 rows. **(3 points)**
# 
# 
# **Q3.b** Create a second dataframe *cereal_df_new* from *cereal_df*, that only includes the columns *name*, *protein*,	*fat*, *fiber*,	*carbo*, *potass*,	*vitamins*,	and *rating*. Then show the first 7 rows of *cereal_df_new*.  **(3 points)**
# 
# **Q3.c** Using dataframe *cereal_df_new* show the cereals with a rating 60 and higher. **(3 points)**
# 
# **Q3.d** Using dataframe *cereal_df_new* show the cereals with the lowest and highest ratings. **(3 points)**
# 
# *Hint: you can use head() function to show first n rows.*

# In[46]:


import pandas as pd

# Q3.a 
cereal_df= pd.read_csv('cereal.csv',sep=';')

cereal_df.head(7)




# In[48]:


# Q3.b
#rating has two commas for some reason
cereal_df_new= cereal_df[['name','protein','fat','fiber','carbo','potass','vitamins','rating,,']]
cereal_df_new.head(7)


# In[64]:


# Q3.c

print(cereal_df_new[cereal_df_new['rating,,']>'60.0'])


# In[96]:


# Q3.d

def maxF(x):
    return x.max()

def minF(x):
    return x.min()       
    

print(cereal_df_new.apply(maxF,axis=0))
print(cereal_df_new.apply(minF,axis=0))


# In[ ]:




