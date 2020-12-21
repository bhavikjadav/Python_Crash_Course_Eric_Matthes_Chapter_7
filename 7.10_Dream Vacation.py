#!/usr/bin/env python
# coding: utf-8

# # 7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

# In[3]:


responses = {}

while True:
    dreamPlace = input("Enter your dream vacation : ")
    onePlace = input("If you could visit one place in the world, where would you go?")
    
    responses[dreamPlace] = onePlace
    
    repeat = input("Would you like to take another poll ? (yes/no)")
    if repeat == "no":
        break


# In[4]:


# print(responses)

