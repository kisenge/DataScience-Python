#!/usr/bin/env python
# coding: utf-8

# # Hands-on 4
# 
# ### CS2545 - Data Science ###
# ### Winter, 2023 ###
# ### UNB, Fredericton ###
# 
# Please complete the following and submit this notebook (filename: handson4-**lastname**-**firstname**.ipynb) to D2L by **11:59 PM, Monday, March 13th**.
# </br>
# </br>
# **NOTE: Late submissions will NOT be accepted and graded as ZERO (0)** 
# </br>
# </br>
# </br>

# **Q1.** Download *user.csv*  from D2L. The entries in *user*  represent movie reviewers.
# 
# Add a column to the dataframe called *agegroups*, where the values of *agegroups* are the labels based on the following table. **(5 points)**
# 
# Infant:      >=0  and <1 <br>
# Toddler:     >=1  and <3 <br>
# Preschooler: >=3  and <6 <br>
# Children:    >=6  and <12 <br>
# Teen:        >=12 and <19 <br>
# Young-adult: >=19 and <25 <br> 
# Adult:       >=25 and <65 <br>
# Senior:      >=65 and <110 <br>
# 
# So, someone aged 13 will be labeled as 'Teen' and someone aged 30 will be labeled as 'Adult'

# In[3]:


import pandas as pd
import numpy as np

u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
user = pd.read_csv('user.csv', sep='|', names=u_cols)

print(user['age'])

#user.iloc[[1],[1]]='ageless'
user['agegroup']=np.nan

for x in range(len(user.index)):
    age= user.values[[x],[1]]
    age=age[0]
    
    #age=int(age)
    if age<1:
        user.iloc[[x],[5]]='Infant'
    
    if age>=1 and age<3:
        #user.iloc[[x],[5]]='Toddler'
        user.loc[x,['agegroup']]='Toddler'
        
    if age>=3 and age<6:
        user.loc[x,['agegroup']]='Preschooler'  
    
    if age>=6 and age<12:
        user.loc[x,['agegroup']]='Children'   
        
    if age>=12 and age<19:
        user.loc[x,['agegroup']]='Teen'   
        
    if age>=19 and age<25:
        user.loc[x,['agegroup']]='Young Adult'   
    
    if age>=25 and age<65:
        #user.loc[x,['agegroup']]='Adult'
        user.loc[x,['agegroup']]='Adult'
    
    if age>=65 and age<110:
        user.iloc[[x],[5]]='Senior'
        
    
        
    
    
   # else:
        #user.iloc[[x],[5]]='invalid'
    
print(user['agegroup'])

# write your code below


# **Q2.1**  Download the **rating.csv**  from D2L. The entries in *rating* represents the movie ratings given by these reviewers. 
# Also, you will need the *user* dataframe with column *agegroups* from  Q1. 
# </br>
# Join these two dataframes to create a new data frame. **(3 points)**
# </br>
# </br>
# **Q2.2**  Print the movie ids of the top rated movies (rating > 4) that are rated by Teens. **(3 points)**
# </br>
# </br>
# **Q2.3**  Print the movie ids of the top rated movies (rating > 4) that are rated by Adults. **(3 points)**
# </br>
# </br>

# In[4]:


import pandas as pd
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
rating = pd.read_csv('rating.csv', sep='\t', names=r_cols)

# write your code below

# Q2.1
#joinedDf= pd.merge(user,rating,on='user_id')
#joinedDF= pd.concat([rating,user])
joinedDf= pd.merge(rating,user,how='left')
print(joinedDf)


# Q2.2


new= joinedDf[(joinedDf['rating']>4)&(joinedDf['agegroup']=='Teen')]
print(new)
print(new["movie_id"])


# Q2.3
new= joinedDf[(joinedDf['rating']>4)&(joinedDf['agegroup']=='Adult')]
print(new)
print(new["movie_id"])



# **Q3.**  Using the dataframe in Q2.1, show the average movie rating for each agegroup. *Also, remove records with NaN fields.* **(6 points)**
# 
# 
# 

# In[ ]:


# write your code below
#
#
#Works but very slow after teen score is calculated
#


infant= joinedDf[(joinedDf['agegroup']=='Infant')]
score=0
for x in range(len(infant)):
    scoreIn= infant.values[[x],[2]]
    score+= (scoreIn[0])/len(infant)
    
print("The average infant score is", score)



toddler= joinedDf[(joinedDf['agegroup']=='Toddler')]
score=0
for x in range(len(toddler)):
    scoreIn= toddler.values[[x],[2]]
    score+= (scoreIn[0])/len(toddler)
    
print("The average toddler score is", score)



preschooler= joinedDf[(joinedDf['agegroup']=='Preschooler')]
score=0
for x in range(len(preschooler)):
    scoreIn= preschooler.values[[x],[2]]
    score+= (scoreIn[0])/len(preschooler)
    
print("The average preschooler score is", score)



children= joinedDf[(joinedDf['agegroup']=='Children')]
score=0
for x in range(len(children)):
    scoreIn= children.values[[x],[2]]
    score+= (scoreIn[0])/len(children)
    
print("The average children score is", score)




teen= joinedDf[(joinedDf['agegroup']=='Teen')]
score=0
for x in range(len(teen)):
    scoreIn= teen.values[[x],[2]]
    score+= (scoreIn[0])/len(teen)
    
print("The average teenage score is", score)



young= joinedDf[(joinedDf['agegroup']=='Young Adult')]
score=0
for x in range(len(young)):
    scoreIn= young.values[[x],[2]]
    score+= (scoreIn[0])/len(young)
    
print("The average young adult score is", score)


adult= joinedDf[(joinedDf['agegroup']=='Adult')]
score=0
for x in range(len(adult)):
    scoreIn= adult.values[[x],[2]]
    score+= (scoreIn[0])/len(adult)
    
print("The average adult score is", score)


senior= joinedDf[(joinedDf['agegroup']=='Senior')]
score=0
for x in range(len(senior)):
    scoreIn= senior.values[[x],[2]]
    score+= (scoreIn[0])/len(senior)
    
print("The average senior score is", score)


# In[ ]:





# In[ ]:




