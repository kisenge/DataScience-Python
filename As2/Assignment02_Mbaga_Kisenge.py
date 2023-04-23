#!/usr/bin/env python
# coding: utf-8

# # Assignment 2
# 
# ### CS2545 - Data Science ###
# ### Winter, 2023 ###
# ### UNB, Fredericton ###
# 
# **Notebook:** Complete the assignment and submit the .ipynb file (with filename changed to **Assignment02_LastName_FirstName.ipynb**) to D2L. <br>
# <br>
# **Deadline:** Tue, April 11, 2023 11:59 pm
# <br>
# <br>
# **Submission guidelines:** <br>
# •	Late submissions until *Wed, April 12, 2023 11:59 pm* will be marked with a **5% penalty**. <br>
# •	All assignment components must be submitted via D2L. <br>
# 
# **Note about plagiarism:** <br>
# Any assignments that appear to be in violation of an academic offence (**plagiarism**) will be reported to the Registrar’s Office as per UNB regulations (See section VII of UNB Undergraduate Calendar). <br>
# 

# **Task and Dataset** 
# 
# For this assignment you will analyze Spotify datasets and perform music related analysis. You will find the following 3 files  in the datasets.zip file from D2L:
# 
# - *artists.csv*
# - *albums.csv*
# - *tracks.csv*
# 
# You may want to first open the files with a text editor and observe the files carefully, to get an idea about the fields in the data table. The meaning of each column label is self-explanatory.

# In[71]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import thinkstats2
import thinkplot
get_ipython().run_line_magic('matplotlib', 'inline')


# **Q1** Load the 3 data files (mentioned above) as dataframes: *artist_df*, *album_df* and *track_df* respectively. 
# 
# Then, show the first 5 records of the dataframes. (**1 points**)

# In[72]:


# load artist_df  dataframe

artist_df = pd.read_csv('artists.csv', delimiter=',')
artist_df.head(5)


# In[73]:


# load album_df  dataframe
album_df = pd.read_csv('albums.csv', delimiter=',')
album_df.head(5)


# In[74]:


# load track_df  dataframe

track_df = pd.read_csv('tracks.csv', delimiter=',')
track_df.head(5)


# **Q1.1** Merge the *artist_df* and *album_df* dataframes and name the new dataframe *artist_album_df* and show the first 5 rows. (**1 points**)

# In[75]:


# your code 
artist_album_df = pd.merge(artist_df,album_df,'inner')
track_df.head(5)


# **Q1.2** Show the name of the artists and number of albums for the **top 10 artists** with the most number of albums (**not singles**). (**2 points**)

# In[76]:


# your code 
singles_df= album_df[album_df['album_type']=='single']
singles_df['artist_id'].value_counts().head(10)


#singles_df['artist_id'].value_counts().index.tolist()


# **Q1.3** How many singles and how many albums were released by **Bruno Merz** since 2010 (inclusive). **(2 points)**
# 
# Note that the release date of albums can be a year or a particular date.

# In[77]:


# your code 
bruno= artist_df[artist_df['artist_name']=="Bruno Mars"]
bruno_id= bruno['artist_id']


# **Q2.1** Who are the top 10 artists with the most popularity? Do these artists have the most followers? If the lists of artists differ, what does that mean? 
# 
# Use *artist_df* to answer this question. (**2 points**)

# In[78]:


# your code for  top 10 artists with the most popularity
artist_df = pd.read_csv('artists.csv', delimiter=',')
artist_df2= artist_df




for i in range(10):
    popsi= artist_df2['artist_popularity'].nlargest(1).index
    popsi2=popsi[0]
  
    pops= artist_df2['artist_popularity'].nlargest(1).values
   
    maxPops= pops[0]
    #print(maxPops)
    pop_df= artist_df2[artist_df2['artist_popularity']==maxPops]
    
    
    artist_df2.drop(popsi2,inplace=True)
   
    print(pop_df['artist_name'])
    
    
    #pop_df.drop()
    

    
        


# In[79]:


# your code for artists having the most followers
artist_df = pd.read_csv('artists.csv', delimiter=',')
artist_df2= artist_df




for i in range(10):
    popsi= artist_df2['followers'].nlargest(1).index
    popsi2=popsi[0]
  
    pops= artist_df2['followers'].nlargest(1).values
   
    maxPops= pops[0]
    #print(maxPops)
    pop_df= artist_df2[artist_df2['followers']==maxPops]
    
   
    artist_df2.drop(popsi2,inplace=True)
   
    print(pop_df['artist_name'])
    


# **Answer:** 

# **Q2.2** Using *artist_df* create a list called *genres* containing all possible values within the "genre" column. This list must contain only unique values.
# 
# *Hint*: the genres column contains strings, not lists. (**2 points**)

# In[80]:


# your code

x=artist_df['genres'].unique()
print(x)


# **Q2.3** Using *artist_df* create 5 new dataframes *pop_df*, *rock_df*, *jazz_df*, *indie_df* and *hiphop_df*. If the genre of a track **contains** the word "pop" (such as, in "danish pop rock"), add it to the *pop_df*. Do this (i.e. create the corresponding dataframes) in a  similar way for other genres. (**2 points**)
# 

# In[81]:


# your code

pop_df= artist_df[artist_df['genres'].str.contains('pop', regex=False)]
print(pop_df)

jazz_df= artist_df[artist_df['genres'].str.contains('jazz', regex=False)]
print(jazz_df)

hiphop_df= artist_df[artist_df['genres'].str.contains('hip hop', regex=False)]
print(hiphop_df)

indie_df= artist_df[artist_df['genres'].str.contains('indie', regex=False)]
print(indie_df)

rock_df= artist_df[artist_df['genres'].str.contains('rock', regex=False)]
print(rock_df)


# **Q2.4** For each of the 5 categories from Q2.3, plot the boxplots of the artist popularity in a single plot. Which genre has the highest median artist popularity and which boxplot looks like it has the lowest number of outliers? How do you know? (**2 points**)

# In[82]:


# your code


plt.subplot(1, 5, 1)
dataPop= pop_df['artist_popularity']
plt.boxplot(dataPop)

plt.subplot(1, 5, 2)
dataRock= rock_df['artist_popularity']
plt.boxplot(dataRock)

plt.subplot(1, 5, 3)
dataJazz= jazz_df['artist_popularity']
plt.boxplot(dataJazz)

plt.subplot(1, 5, 4)
dataHiphop= hiphop_df['artist_popularity']
plt.boxplot(dataHiphop)

plt.subplot(1, 5, 5)
dataIndie= indie_df['artist_popularity']
plt.boxplot(dataIndie)

#hip hop has the highest popularity level becuase its median is highest and it seems like jazz has the lowest number of outliers
#becuase it has the shortest whiskers


# **Answer:** 

# **Q2.5** For each of the 5 categories from Q2.3, plot a bar chart of the number of followers per given genre (pop, rock, jazz, indie and hip hop) in a single plot. Which genre has the most followers? Which one has the least? (**2 points**)

# In[83]:


# your code


plt.subplot(1, 5, 1)
dataPop= pop_df['artist_popularity']

popFollowers= pop_df['followers'].sum()
rockFollowers= rock_df['followers'].sum()
jazzFollowers= jazz_df['followers'].sum()
hiphopFollowers= hiphop_df['followers'].sum()
indieFollowers= indie_df['followers'].sum()

data=[popFollowers,rockFollowers,jazzFollowers,hiphopFollowers,indieFollowers]



x= [i for i in range(1,6)]
plt.bar(x,data)


    



# **Answer:** 

# **Q3.** Danceability has been defined as a property that indicates how suitable a piece of music is to dance based on various audio features such as tempo, loudness, valence (i.e. musical positiveness of emotion) and speechiness etc. In the next few questions, you will try to determine the features that have the most influence on danceability.
# 
# Use *track_df* to answer these questions. Filter out any record with danceability 0 or less, before proceeding.

# **Q4.1** Plot a scatterplot of the danceability of the tracks (on the x-axis) and their tempo (on the y-axis), then calculate Pearson’s Correlation Coefficient. (**1 points**)

# In[84]:


# your code
new_track_df= track_df[track_df['danceability']!=0]
plt.scatter(new_track_df['danceability'],new_track_df['tempo'])

thinkstats2.Cov(new_track_df['danceability'],new_track_df['tempo'])/(thinkstats2.Std(new_track_df['danceability'])*thinkstats2.Std(new_track_df['tempo']))



# **Q4.2** Plot a scatterplot of the danceability of the tracks (on the x-axis) and their valence (on the y-axis), then calculate Pearson’s Correlation Coefficient. (**1 points**)

# In[85]:


# your code
new_track_df= track_df[track_df['danceability']!=0]
plt.scatter(new_track_df['danceability'],new_track_df['valence'])

thinkstats2.Cov(new_track_df['danceability'],new_track_df['valence'])/(thinkstats2.Std(new_track_df['danceability'])*thinkstats2.Std(new_track_df['valence']))



# **Q4.3** Plot a scatterplot of the danceability of the tracks (on the x-axis) and their loudness (on the y-axis), then calculate Pearson’s Correlation Coefficient. (**1 points**)

# In[86]:


# your code

new_track_df= track_df[track_df['danceability']!=0]
plt.scatter(new_track_df['danceability'],new_track_df['loudness'])

thinkstats2.Cov(new_track_df['danceability'],new_track_df['loudness'])/(thinkstats2.Std(new_track_df['danceability'])*thinkstats2.Std(new_track_df['loudness']))



# **Q4.4** From the above plots, what can you infer? Which feature of a track has the most influence on its danceability? (**1 point**)

# **Answer:** 

# In[87]:


#It seems like loudness is the most influential factor. Tempo is also quite helpful and valence is quite useless for 
#predicting dancability.

