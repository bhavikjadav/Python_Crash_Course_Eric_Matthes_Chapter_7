#!/usr/bin/env python
# coding: utf-8

# # 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

# In[1]:


prompt = "Pizza toppings : "
message = ""
while message != "quit":
    message = input(prompt)
    print(message)

