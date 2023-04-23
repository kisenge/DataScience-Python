#!/usr/bin/env python
# coding: utf-8

# # Hands-on 2
# 
# ### CS2545 - Data Science ###
# ### Winter, 2023 ###
# ### UNB, Fredericton ###
# 
# Please complete the following and submit this notebook (filename: handson2-**lastname**-**firstname**.ipynb) to D2L by 11:59 pm, Friday, February 10. 
# </br>
# </br>
# </br>

# **1.**  Download the *cereal.csv* file from D2L in the current folder. This includes information about the per serving nutritional content of a number of breakfast cereals. The columns in this file represent the following fields (detail and short) and data types: <br>
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
# Write a program to read the CSV file and answer the following questions:
# 
# **1.a** Which manufacturer(s) produces the most number of cereal? (**2 points**)
# 
# **1.b** Which cereal(s) have the highest calories per serving? (**2 points**)
# 
# **1.c** Which cereal(s) have the highest sugar per serving? (**2 points**)
# 
# **1.d** What are the five most popular and five least popular cereals according to the ratings? (i.e., higher rating means more popular) (**4 points**)
# 

# In[143]:


import csv
# save the results as a list of elements
cereal_most_manufacturer = []
cereal_highest_calories_name = []
cereal_highest_sugar_name = []
cereal_most_popular = []
cereal_least_popular = []

# write your code below
# start - your code

#1.a

with open("cereal.csv","r") as file:
    content= csv.reader(file,delimiter=";")
    
    lineCount=0
    lineCount=lineCount-1
    
    name=[]
    mfr=[]
    
    for line in content:
        #print(line)
        name.append(line[0])
        mfr.append(line[1])
        
    #print(mfr)
    #print(name)
    
    uniqueProduct= []
    
    
    for company in mfr:
        nameList=[]
        for names in name:
        
            if name in nameList:
                pass
            else:
                nameList.append(name)
                uniqueProduct.append(company)
                
    coList=[]
    coListCount=[]
    max=0
    for company in uniqueProduct:
        if company in coList:
            pass
        
        else:
            
            num= uniqueProduct.count(company)
            coListCount.append(num)
            
            if num>max:
                max=num
            coList.append(company)
            
    pos=0
    for elem in coListCount:
        if elem ==max:
            cereal_most_manufacturer.append(coList[pos])
        pos=pos+1  
        


#1.b
with open("cereal.csv","r") as file:
    content= csv.reader(file,delimiter=";")
    
    lineCount=0
    lineCount=lineCount-1
    
   
    
    max=0
    cal=0
    pos=0
    calList=[]
    lst=[]
    
    
    for line in content:
        if(pos!=0):
            #print(line)
            lst.append(line)
            cal= int(line[3])
            if cal>max:
                calList=[]
                max=cal
                calList.append(max)
        pos=pos+1
            
    for elem in lst:
        
        if int(elem[3])==max:
            cereal_highest_calories_name.append(elem[0])
        
          
   
        

#1.c

with open("cereal.csv","r") as file:
    content= csv.reader(file,delimiter=";")
    
   
    max=0
    sug=0
    pos=0
    sugarList=[]
    lst=[]
    
    
    for line in content:
        if(pos!=0):
            #print(line)
            lst.append(line)
            sug= int(line[9])
            if sug>max:
                sugarList=[]
                max=sug
                sugarList.append(max)
        pos=pos+1
            
    for elem in lst:
        
        if int(elem[9])==max:
            cereal_highest_sugar_name.append(elem[0])
        
          
   
        


#1.d.a
with open("cereal.csv","r") as file:
    content= csv.reader(file,delimiter=";")
    
   
    max=0
    rating=0
    pos=0
    ratingList=[]
    lst=[]
    
    
    for line in content:
        if(pos!=0):
            #print(line)
            lst.append(line)
            rating= float(line[15])
            ratingList.append(rating)
            
        pos=pos+1
    ratingList.sort()
    ratingList.reverse()
    
    
    
    for elem in lst:
        if float(elem[15]) in ratingList[0:5]:
            cereal_most_popular.append(elem[0])
            
            

#1.d.b
with open("cereal.csv","r") as file:
    content= csv.reader(file,delimiter=";")
    
   
    max=0
    rating=0
    pos=0
    ratingList=[]
    lst=[]
    
    
    for line in content:
        if(pos!=0):
            #print(line)
            lst.append(line)
            rating= float(line[15])
            ratingList.append(rating)
            
        pos=pos+1
    ratingList.sort()
    
    
    
    
    for elem in lst:
        if float(elem[15]) in ratingList[0:5]:
            cereal_least_popular.append(elem[0])
            

            
            

            
            


        
# end - your code 





# test

print ("The name(s) of the manufacturer(s) producing the most number of cereal:",  cereal_most_manufacturer)
print ("The name of the cereal(s) with highest calories:",  cereal_highest_calories_name)
print ("The name of the cereal(s) with highest sugar:",  cereal_highest_sugar_name)
print ("The name of the five most popular cereals:",  cereal_most_popular)
print ("The name of the five least popular cereals:",  cereal_least_popular)
print ("\n")


# **2.**  Download the file *ihockeychampions.json* from D2L. It contains info about the winners of the Ice Hockey World Championships from 2001 to 2021. 
# 
# First, open the JSON file and deserialize it using JSON API to construct a corresponding Python object. 
# 
# Then, 
# 
# **2.a** Write a program to process the data and print the years in which Sweden won the gold medal. (**5 points**)
# 
# **2.b** Write a program to find the country who won the gold medal most, and how many times? (**5 points**)
# 

# In[144]:


#Kisenge Mbaga
# write your code below
import json
from statistics import mode

#2.a
f= open("ihockeychampions.json")
data= json.load(f)

keys= data.keys()

for i in keys:
    if(data[i]['gold']=="Sweden"):
        print(i)

f.close()


#2.b
f= open("ihockeychampions.json")
data= json.load(f)
keys= data.keys()
goldWinners= []


for i in keys:
    goldWinners.append(data[i]['gold'])
    
x= mode(goldWinners)

count=0
for i in keys:
    if(data[i]['gold']==x):
        count=count+1

print(x+" has won ",count," times.")

f.close()



# your code - end


# In[ ]:




