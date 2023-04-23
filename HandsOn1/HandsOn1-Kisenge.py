#!/usr/bin/env python
# coding: utf-8

# # Hands-on 1
# 
# ### CS2545 - Data Science ###
# ### Winter, 2023 ###
# ### UNB, Fredericton ###
# 
# Please complete the following tasks per instructions provided. Please complete the following and submit this notebook (filename: handson1-lastname-firstname.ipynb) on D2L by 11:59pm, January 27. 
# </br>
# </br>
# </br>
# 

# **[1.]** The list *polygons_list* below contains the names of the polygons with the number sides varied from 3 to 15. For instance, Triangle is a polygon with 3 sides, Hexagon is a polygon with 6 sides.
# 
# **[1.a]** Using "list slicing" print first 5 and last 4 entries in *polygons_list*. **[4 points]**
# 
# 
# **[1.b]** Write Python code that iterates over the elements of *polygons_list* and prints each element (i.e. as a string), its number of sides, and its sum of angles. **[6 points]**
# 
# Example output: <br>
# Triangle: 3 -> 180 <br>
# Square: 4 -> 360 <br>
# Pentagon: 5 -> 540 <br>

# In[1]:


polygons_lst = ['Triangle', 'Square', 'Pentagon', 'Hexagon', 'Heptagon', 'Octagon', 'Nonagon', 'Decagon', 'Hendecagon', 'Dodecagon', 'Tridecagon', 'Tetradecagon', 'Pentadecagon']

# write your code below

# 1.a) 

print(polygons_lst[:4])
print(polygons_lst[9:])



# 1.b) 
sides=3
angle=180

for elem in polygons_lst:
    
    print(elem + ": ",sides, "-> ",angle)
    sides= sides+1
    angle= angle+180
    


# **Example code**  The following code snippet uses Python graphics library Turtle. Execute the code. There will be a pop-up window where the image will be rendered.
# 
# More info about Turtle library is here: https://docs.python.org/3.8/library/turtle.html

# In[2]:


import turtle




polygon = turtle.Turtle() 
  
    
side_length = 100
angle = 360.0 / 3  
  
polygon.forward(side_length) 
polygon.right(angle) 

polygon.forward(side_length) 
polygon.right(angle) 

polygon.forward(side_length) 
polygon.right(angle) 


# close resources properly 
# https://stackoverflow.com/questions/7217405/turtle-graphics-not-responding
polygon.hideturtle()
turtle.done() 
try:
    turtle.bye()   
except turtle.Terminator:
    pass


# **2.** Modify the example code above. Write code to draw a polygon with the number of sides based on user input *Sides* where *Sides* is the number of sides in the polygon to draw. Your code should do the following.
# 
# First, print the name of the polygon representing the polygon with number of sides based on user input (e.g. 'Square' for number of sides as 4).
# 
# Then, draw a polygon with the number of sides based on user input. **[10 points]**

# In[15]:


import turtle

polygon = turtle.Turtle() 

side_length = 100
polygons_lst = ['Triangle', 'Square', 'Pentagon', 'Hexagon', 'Heptagon', 'Octagon', 'Nonagon', 'Decagon', 'Hendecagon', 'Dodecagon', 'Tridecagon', 'Tetradecagon', 'Pentadecagon']

Sides = input("Input Number of Sides:")
num_sides = int(Sides)

print ("Number of Sides =", num_sides)

if num_sides not in range (3,16):
    print ("Out of Range")
else:    

    # write your code below
   
    
    # print the name of the polygon with the user specified number of sides
    if num_sides==3:
        name= polygons_lst[0]
        
    else:
        sub= num_sides-3
        name=  polygons_lst[sub]
    
    print ("The Name of the Polygon is: ", name)
   
    if(num_sides)==3:
            angle=180
            
    else:
        angle= ((num_sides-3)*180)+180
        angle= angle/num_sides
        angle= 180-angle
    # draw the polygon with the user specified number of sides
    for x in range(num_sides+1): 
        polygon.forward(side_length)
        polygon.right(angle)
    
    
# close resources properly 
# https://stackoverflow.com/questions/7217405/turtle-graphics-not-responding
polygon.hideturtle()
turtle.done() 
try:
    turtle.bye()   
except turtle.Terminator:
    pass


# In[ ]:




