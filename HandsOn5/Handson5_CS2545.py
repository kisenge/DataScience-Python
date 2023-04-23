#!/usr/bin/env python
# coding: utf-8

# # Hands-on 5
# 
# ### CS2545 - Data Science ###
# ### Winter, 2023 ###
# ### UNB, Fredericton ###
# 
# Please complete the following and submit this notebook (filename: handson5-**lastname**-**firstname**.ipynb) to D2L by **11:59 pm, Monday, March 27th**. 
# </br>
# </br>
# </br>

# **Q1.** Download *user.csv*  from Hands-on4 (also, provided with this Hands-on). The entries in *user*  represent movie reviewers.
# 
# Then download the *rating.csv* from Hands-on4 (also, provided with this Hands-on). The entries in *rating* represents the movie ratings given by these reviewers. 
# 
# 
# Finally, join these two data frames to create a new data frame *rated_by*. **(2 points)**

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
user = pd.read_csv('user.csv', sep='|', names=u_cols)

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
rating = pd.read_csv('rating.csv', sep='\t', names=r_cols)

# write your code below
rated_by= pd.merge(rating,user,how='inner')
print(rated_by)


# **Q1.1.**  Plot a chart with two subplots in a  2 x 1 (i.e. 2 rows and 1 column) layout. Hence, there will be two subplots one on top of the other. The x-axis label should be 'occupation' and shared by both the subplots. The title should appear above the top subplot and it will be 'Movie Ratings by Occupation'. **(4 + 4 = 8 points)**
# 
# In the top subplot, plot a bar graph of the **number of movie rating** attributed to each occupation. The y-axis label should be  'rating count'.
# 
# In the bottom subplot, plot a bar graph of the **average movie rating** attributed to each occupation. The y-axis label should be  'average rating'.

# In[ ]:


# write your code below
xpop = [1,2,3,4]
ypop = [x for x in range(943)]



rateNums=rated_by.occupation.value_counts()
#occs=rated_by.occupation.mode()
#occs=rated_by['occupation'].value_counts().nlargest(21)
occs= rated_by['occupation'].value_counts().keys()[0:21]
print(rateNums)
print(occs)
f, axes = plt.subplots(2, sharex=True)
occsList=occs.tolist()
rnList=rateNums.tolist()

avg=[]
cnt=-1

#for x in occsList:
    #cnt=cnt+1
    #for k in range(len(rated_by)):
        #occ= rated_by.values[[k],[6]]
        #occ=occ[0]
        #if occ==x:
            #avg[cnt]=avg[cnt]+1
#for k in range(len(rated_by)):
    #occ= rated_by.values[[k],[6]]
    #occ=occ[0]
    #if occ=='student':
        #avg[cnt]=avg[cnt]+1
        #print("hey")
    #else:
        #print("wtf")
        

use =rated_by[rated_by['occupation'] == 'student']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'other']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'educator']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'engineer']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'programmer']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'administrator']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'writer']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'librarian']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'technician']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'executive']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'healthcare']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'artist']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'entertainment']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'scientist']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'marketing']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'retired']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'lawyer']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'none']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'salesman']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'doctor']
sum= use['rating'].sum() 
avg.append(sum/len(use))

use =rated_by[rated_by['occupation'] == 'homemaker']
sum= use['rating'].sum() 
avg.append(sum/len(use))

#print(avg)
            
f.suptitle("Movie Ratings by Occupation")
axes[0].bar(occs,rateNums)
axes[0].set_ylabel('rating count')
axes[1].bar(occs,avg)
axes[1].set_ylabel('average rating')


# **Q2.** The purpose of this question is to familiarize you with the  National Survey of Family Growth (NSFG) dataset used in the textbook. 
# 
# Download the codendata.zip by running the commands below in a Terminal shell (on Linux) or clicking the link (on Windows): <br>
# wget www.cs.unb.ca/~sray/teaching/datascience/codendata.zip <br>
# 
# After you unzip it, you will find several files related to code and NSFG dataset. Copy those files in the current folder.
# 

# In[1]:


# then, execute this code cell

import nsfg

nsfg_df = nsfg.ReadFemPreg()

nsfg_df.head(5)



# **Q2.1** After loading the NSFG dataset, plot a boxplot  of the birth weights for live births. The corresponding column in the data frame is called *birthwgt_lb*. **(5 points)**

# In[2]:


# write your code below

#nsfg_df.plot(kind='bar', x='birthwgt_lb', color='green')
boxplot = nsfg_df.boxplot(column=['birthwgt_lb'])
boxplot.plot()



# **Q2.2** 
# Using *thinkstats2* APIs calculate Q1 and Q3 of the birth weights for live births (using the dataframe in Q2.1). Then, calculate the IQR of the  birth weights for live births. **(5 points)**
# 
# *Hint:* Refer to class notes on percentile and percentile rank APIs from Cdf object.

# In[1]:


import thinkstats2
import thinkplot

# write your code below
cdf=thinkstats2.Cdf(nsfg_df.birthwgt_lb, label="Q1")

thinkplot.PrePlot(2)
thinkplot.Config(title="title")
thinkplot.Cdfs([cdf])

Q1=cdf.Percentile(25)
print("Q1: ",Q1)

Q3=cdf.Percentile(75)
print("Q3: ",Q3)

IQR= Q3-Q1
print("IQR: ",IQR)


# In[ ]:




