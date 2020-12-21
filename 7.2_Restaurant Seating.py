#!/usr/bin/env python
# coding: utf-8

# # 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

# In[1]:


dinner_group = int(input("How many peoples are in your dinner group ? "))


# In[2]:


if dinner_group > 8:
    print("Sir, You have to wait for a table.")
else:
    print("Your table is ready.")

