#!/usr/bin/env python
# coding: utf-8

# # 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

# In[7]:


number = int(input("Enter a number i will tell you whether the number is multiple of ten or not : "))


# In[8]:


if  number%10 == 0:
    print("Yes, number is multiple of ten.")
else:
    print("No, No.")

