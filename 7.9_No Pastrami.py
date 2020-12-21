#!/usr/bin/env python
# coding: utf-8

# # 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

# In[4]:


sandwitch_orders = ["chhese", "veg", "pastrami", "non-veg", "pastrami", "diet", "pastrami"]
finished_sandwitches = []


# In[5]:


print("The Deli has run out of Pastrami.")
for sandwitch_order in sandwitch_orders:
    while "pastrami" in sandwitch_orders:
        sandwitch_orders.remove("pastrami")
    
    print("I made your " + sandwitch_order.title() + " sandwitch.")
    finished_sandwitches.append(sandwitch_order)


# In[6]:


for sandwitch in finished_sandwitches:
    print("Your " + sandwitch.title() + " sandwitch is ready.")


# In[7]:


print(sandwitch_orders)


# In[8]:


print(finished_sandwitches)

