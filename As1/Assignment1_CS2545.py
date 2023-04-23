#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# 
# ### CS2545 - Data Science ###
# ### Winter, 2023 ###
# ### UNB, Fredericton ###
# 
# Please complete the following and submit this notebook (filename: Assignment1-**lastname**-**firstname**.ipynb) on D2L by **Monday, March 20th, 11:59 PM**.
# </br>
# </br>
# **NOTE:**
# </br>
# **Late submissions will be accepted until Tuesday, March 21st, 11:59 PM**
# </br>
# **Late submissions will be evaluated with a PENALTY of 10%**
# </br>
# </br>

# **Q1** Download the *countries.csv* and *world_gdp_2019.csv* files from D2L in the current folder. Load them into two dataframes *country* and *gdp*. Show top 5 countries in terms of gdp (based on column 'GDP_US$' in *gdp*). **(2 points)**

# In[188]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Load countries.csv
u_cols = ['country', 'population', 'area', 'currency']
country = pd.read_csv('countries.csv', sep=';', names=u_cols)
print(country)

u_cols1 = ['country', 'code', 'gdp']
gdp = pd.read_csv('world_gdp_2019.csv', sep=';', names=u_cols1, skiprows=[0])

gdpCopy= gdp
gdpCopy2= gdp

#for i in range(5):
#c= gdp['gdp'].astype(float).min()
print("Maximum GDPs:")
for i in range(5):
    c= gdpCopy['gdp'].astype(float).idxmax()
    print(gdpCopy.iloc[c])
    gdpCopy.drop(c, inplace=True)



# **Q1.1** Using the dataframes created in Q1.0, answer the following. **(1+1 = 2 points)**
# 
# * A. Create a dataframe *country_gdp* that shows the countries and their GDPs by **joining** the two dataframes above. 
# Note that you need to show all the countries in *country* dataframe even if there is no information in *gdp* dataframe.
# 
# * B. Remove the rows where the *GDP_US$* columns shows a *NaN* value. 

# In[152]:


# Q1.1 A

joinedDf= pd.merge(country,gdp,how='left')
print(joinedDf)


# In[317]:


# Q1.1 B
import numpy as np
joinedDf= pd.merge(country,gdp,how='outer')
 

joinedDf.dropna(subset=['gdp'],inplace=True)
print(joinedDf)

       
        




# **Q2.1** Add a column **IncomeGroup** to the dataframe **country_gdp** based on the GDP of the country and GDP ranges and the corresponding income group labels below. **(2 points)**
# 
# <style type="text/css">
# .tg  {border-collapse:collapse;border-spacing:0;}
# .tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
# .tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
# .tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
# .tg .tg-0lax{text-align:left;vertical-align:top}
# </style>
# <table class="tg">
#   <tr>
#     <th class="tg-1wig" colspan="2"> GDP range</th>
#     <th class="tg-0lax" rowspan="2">Income group</th>
#   </tr>
#   <tr>
#     <td class="tg-1wig">Min GDP</td>
#     <td class="tg-1wig">Max GDP</td>
#   </tr>
#   <tr>
#     <td class="tg-0lax">0</td>
#     <td class="tg-0lax">500000000</td>
#     <td class="tg-0lax">low</td>
#   </tr>
#   <tr>
#     <td class="tg-0lax">500000000</td>
#     <td class="tg-0lax">5000000000</td>
#     <td class="tg-0lax">lower middle</td>
#   </tr>
#   <tr>
#     <td class="tg-0lax">5000000000</td>
#     <td class="tg-0lax">50000000000</td>
#     <td class="tg-0lax">middle</td>
#   </tr>
#   <tr>
#     <td class="tg-0lax">50000000000</td>
#     <td class="tg-0lax">500000000000</td>
#     <td class="tg-0lax">upper middle</td>
#   </tr>
#   <tr>
#     <td class="tg-0lax">500000000000</td>
#     <td class="tg-0lax">50000000000000</td>
#     <td class="tg-0lax">high</td>
#   </tr>
# </table>

# In[318]:


# Q2.1

joinedDf.dropna(subset=['gdp'],inplace=True)
joinedDf["Income Group"]=1
incomeGroup=[]

for i in range(len(joinedDf)):
    num= float(joinedDf.iloc[i,5])
    
    
    if num>0 and num< 5e+8:
        print(num)
        #joinedDf.loc[i+1,"Income Group"]="low"
        incomeGroup.append("low")
    elif num>5e+8 and num<5e+9:
        print(num)
        #joinedDf.loc[i+1,"Income Group"]="lower middle"
        incomeGroup.append("lower middle")
    elif num>5e+9 and num<5e+10:
        print(num)
        #joinedDf.loc[i+1,"Income Group"]="middle"
        incomeGroup.append("middle")
        print("yo middle")
    elif num>5e+10 and num<5e+11:
        print(num)
        #joinedDf.loc[i+1,"Income Group"]="upper middle"
        incomeGroup.append("upper middle")
        print("yo upper")
    elif num>5e+11 and num<5e+13:
        print(num)
        incomeGroup.append("high")
        #joinedDf.loc[i+1,"Income Group"]="high"
        
    #else:
        #joinedDf.loc[i,6]="out"
joinedDf["Income Group"]=incomeGroup
joinedDf.dropna(thresh=4,inplace=True)        
print(joinedDf)  
    

    


# **Q2.2**  Using the dataframe from above, group the countries by *IncomeGroup* column and show the average GDP for each income group. **(2 points)**

# In[320]:


# Q2.2

joinedDf.sort_values(by='Income Group',inplace=True)
#joinedDf.iloc[:50]#to show sorted

joinedDf


# **Q2.3**  Using the dataframe from Q2.1, group the countries by *IncomeGroup* column and plot a bar chart for the median GDP (GDP_US$) for each income group. The y-axis should be in log scale. **(2 points)**

# In[343]:


# Q2.3
import matplotlib.pyplot as plt

medians=[]
lowerMiddleM=0
lowerMiddleInc=0

lowM=0
lowInc=0

highM=0
highInc=0

upperMiddleM=0
upperMiddleInc=0

middleM=0
middleInc=0

joinedDf.sort_values(by='Income Group',inplace=True)
joinedDf.iloc[:50]#to show sorted


for i in range(len(joinedDf)):
    val= joinedDf.iloc[i,6]
    
    if val=="lower middle":
        lowerMiddleInc=lowerMiddleInc+1
        lowerMiddleM+=int(joinedDf.iloc[i,5])
    
    elif val=="middle":
        middleInc=middleInc+1
        middleM+=int(joinedDf.iloc[i,5])
        
    elif val=="upper middle":
        upperMiddleInc=upperMiddleInc+1
        upperMiddleM+=int(joinedDf.iloc[i,5])
        
    elif val=="low":
        lowInc=lowInc+1
        lowM+=int(joinedDf.iloc[i,5])
        
    elif val=="high":
        highInc=highInc+1
        highM+=int(joinedDf.iloc[i,5])
        
        
        
medians.append(lowM/lowInc)
medians.append(lowerMiddleM/lowerMiddleInc)
medians.append(middleM/middleInc)
medians.append(upperMiddleM/upperMiddleInc)
medians.append(highM/highInc)

print(medians)

#plt.bar(medians, logy=True)
data = {'medians':['low','lower middle','middle','upper middle','high'],
'median' :medians}
df = pd.DataFrame(data)
df.plot(kind='bar', x='medians', color='green',logy=True)

#plt.show()


# **Q3** Download the *capitals.csv*  and *major_cities.csv* files from D2L in the current folder. Load them into two dataframes **capital** and **major_cities**, and then show first 5 rows. The major cities are some of the cities with relatively large population. The capitals are capitals of the countries. **(2 points)**
# 

# In[351]:


# Load capitals.csv

u_cols = ['CapitalCity','Country','CountryCode','Latitude','Longitude']
major = pd.read_csv('capitals.csv', sep=',', names=u_cols,skiprows=[0])
print(capitals.iloc[:5])


# In[356]:


# Load major_cities.csv

u_cols = ['City','Country','CityPopulation']
major = pd.read_csv('major_cities.csv', sep=',', names=u_cols,skiprows=[0])
print(major.iloc[:5])


# **Q3.1** For each country that has a Megacity (i.e. city with population more than 10 million), show the name of country and the number of Megacities it has. **(1 point)**
# 
# **Note: Countries should be sorted in descending order based on the number of megacities they have.**

# In[368]:


# Q3.1

major.sort_values(by='CityPopulation',ascending=False, inplace=True)
print(major)
cntryList=[]

for i in range(len(major)):
    if major.iloc[i,2]>10000000:
        cntry= major.iloc[i,1]
        if cntry in cntryList:
            index1=cntryList.index(cntry)
            cntryList[index1+1]=int(cntryList[index1+1])+1
        else:
            cntryList.append(cntry)
            cntryList.append(str(1))
    
for i in range(int(len(cntryList)/2)):
    print(cntryList[i])


# **Q4** For the questions Q4.1 and Q4.3, you will plot data on a map. If you have installed an Anaconda Python distribution in your local machine, you have to install **basemap** and **plotly** packages. If you are using FCS lab VM, then they are already installed in the VMs.
# 

# **Q4.1** From question Q3.0 (for the dataframe **major_cities**), plot the name of the top 10 cities (i.e. by population) in a map of the world. Use the Basemap module for this. For more help, visit https://matplotlib.org/basemap/. **(3 points)**

# In[374]:


import numpy as np
import matplotlib.pyplot as plt
# use the following module 
#from mpl_toolkits.basemap import Basemap
import Basemap from mpl_toolkits.basemap

# Write your code here
m = Basemap(projection='mill',
            llcrnrlat = 25,
            llcrnrlon = -130,
            urcrnrlat = 50,
            urcrnrlon = -60,
            resolution='l')


LAlat, LAlon = 9.05785,7.49508
xpt, ypt = m(LAlon, LAlat)
m.plot(xpt, ypt, 'g^', markersize=15)


# **Q4.2** Add a column **gdp_per_capita** to the dataframe **country_gdp** in Q2.1. This will be a calculated column based on the GDP per capita of each country. **(1 point)**

# In[27]:


# Q4.2


# **Q4.3** Using the above dataframe (which will include *gdp_per_capita*), create a choropleth map of the world based on the GDP per capita of each country. Use the plotly module for this. For more help, visit https://plotly.com/python/choropleth-maps/. **(3 points)**
# 

# In[28]:


import plotly.graph_objects as go
import pandas as pd

# Write your code here

