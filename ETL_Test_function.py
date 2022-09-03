#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install psycopg2')


# In[1]:


import json
import pandas as pd
import numpy as np

import re

from sqlalchemy import create_engine
import psycopg2

# from config import db_password

import time

# 1. Create a function that takes in three arguments;
# Wikipedia data, Kaggle metadata, and MovieLens rating data (from Kaggle)
def results(): 
    # 2. Read in the kaggle metadata and MovieLens ratings CSV files as Pandas DataFrames.
    wiki_movies_df =  pd.read_csv('movies_metadata.csv')
    kaggle_metadata = pd.read_csv('ratings.csv')
    # 3. Open the read the Wikipedia data JSON file.
    with open ('wikipedia-movies.json', mode='r') as file:
    # 4. Read in the raw wiki movie data as a Pandas DataFrame.
        ratings = pd.DataFrame(json.load(file))
    # 5. Return the three DataFrames
    return wiki_movies_df, kaggle_metadata, ratings

# 6 Create the path to your file directory and variables for the three files. 
file_dir = 'C:\GitHub\MODULE8'
# Wikipedia data
wiki_file = f'{file_dir}/wikipedia_movies.json'
# Kaggle metadata
kaggle_file = f'{file_dir}/movies_metadata.csv'
# MovieLens rating data.
ratings_file = f'{file_dir}/ratings.csv'

# 7. Set the three variables in Step 6 equal to the function created in Step 1.
wiki_file, kaggle_file, ratings_file = results()


# In[2]:


print(wiki_file)


# In[3]:


# 8. Set the DataFrames from the return statement equal to the file names in Step 6. 
wiki_movies_df = wiki_file
kaggle_metadata = kaggle_file
ratings = ratings_file


# In[4]:


# 9. Check the wiki_movies_df DataFrame.
wiki_movies_df.head()


# In[5]:


# 10. Check the kaggle_metadata DataFrame.
kaggle_metadata.head()


# In[6]:


# 11. Check the ratings DataFrame.
ratings.head()


# In[ ]:




