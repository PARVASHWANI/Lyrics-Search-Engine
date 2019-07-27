#!/usr/bin/env python
# coding: utf-8

# In[10]:


import json,requests


# In[28]:


print("This Project is developed by Parv Ashwani")
print("__________________________________________")
print("Note:- Only English Songs Are Supported")
print("__________________________________________")


# In[29]:


base_url = "https://api.lyrics.ovh/v1/"
title = input("Enter the Name of the Song: ")
artist = input("Enter the Name of the Artist: ")
complete_url = base_url + artist + '/' + title


# In[30]:


complete_url


# In[31]:


response = requests.get(complete_url)


# In[32]:


data  = response.json()


# In[33]:


print(data['lyrics'])


# In[ ]:

input()


