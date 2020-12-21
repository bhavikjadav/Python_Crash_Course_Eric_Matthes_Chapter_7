#!/usr/bin/env python
# coding: utf-8

# # 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
# # • Use a conditional test in the while statement to stop the loop.
# # • Use an active variable to control how long the loop runs.
# # • Use a break statement to exit the loop when the user enters a 'quit' value.

# In[1]:


Active = True

while Active:
    age = input("Enter your age : ")
    if age == "quit":
        break
    
    age = int(age)
    
    if (age <= 3):
        print("Ticket is free.")
    elif (age > 3) and (age <= 12):
        print("Ticket price is 10$.")
    elif (age > 12):
        print("Ticket price is 15$.")

