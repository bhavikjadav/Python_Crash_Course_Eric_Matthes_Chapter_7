#!/usr/bin/env python
# coding: utf-8

# # 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

# In[11]:


sandwitch_orders = ["chhese", "veg", "non-veg", "diet"]
finished_sandwitches = []


# In[12]:


for sandwitch_order in sandwitch_orders:
    print("I made your " + sandwitch_order.title() + ".")
    finished_sandwitches.append(sandwitch_order)


# In[13]:


for sandwitch in finished_sandwitches:
    print("Your " + sandwitch.title() + " sandwitch is ready.")

