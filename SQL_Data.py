#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sqlalchemy import create_engine


# In[4]:


"postgresql://[user]:[password]@[location]:[port]/[Challenge8]"


# In[6]:


db_password = 'YOUR_PASSWORD_HERE'
from config1 import db_password


# In[7]:


db_string = f"postgresql://postgres:{db_password}@127.0.0.1:5432/Challenge 8"


# In[8]:


engine = create_engine(db_string)


# In[ ]:




