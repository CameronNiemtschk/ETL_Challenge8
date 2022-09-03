#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pandas as pd
import numpy as np

import re

from sqlalchemy import create_engine
import psycopg2

# from config import db_password

import time


# In[5]:


# 1. Add the clean movie function that takes in the argument, "movie".
def clean_movie(movie):
    wiki_movies_df =  pd.read_csv('movies_metadata.csv')
    kaggle_metadata = pd.read_csv('ratings.csv')
    with open ('wikipedia-movies.json', mode='r') as file:
        ratings = pd.DataFrame(json.load(file))
    return wiki_movies_df, kaggle_metadata, ratings
file_dir = 'C:\GitHub\MODULE8'
wiki_file = f'{file_dir}/wikipedia_movies.json'
kaggle_file = f'{file_dir}/movies_metadata.csv'
ratings_file = f'{file_dir}/ratings.csv'


# In[3]:





# In[6]:


# 2 Add the function that takes in three arguments;
# Wikipedia data, Kaggle metadata, and MovieLens rating data (from Kaggle)

# 1. Add the clean movie function that takes in the argument, "movie".
def clean_movie(movie):
    wiki_movies_df =  pd.read_csv('movies_metadata.csv')
    kaggle_metadata = pd.read_csv('ratings.csv')
    with open ('wikipedia-movies.json', mode='r') as file:
        ratings = pd.DataFrame(json.load(file))
    return wiki_movies_df, kaggle_metadata, ratings
file_dir = 'C:\GitHub\MODULE8'
wiki_file = f'{file_dir}/wikipedia_movies.json'
kaggle_file = f'{file_dir}/movies_metadata.csv'
ratings_file = f'{file_dir}/ratings.csv'
    # 3. Write a list comprehension to filter out TV shows.
wiki_movies = [movie for movie in wiki_file
               if ('video' not in movie)]
    # 4. Write a list comprehension to iterate through the cleaned wiki movies list
    # and call the clean_movie function on each movie.
    

    # 5. Read in the cleaned movies list from Step 4 as a DataFrame.
wiki_movies.df

    # 6. Write a try-except block to catch errors while extracting the IMDb ID using a regular expression string and
    #  dropping any imdb_id duplicates. If there is an error, capture and print the exception.
    try:
        
    except 

    #  7. Write a list comprehension to keep the columns that don't have null values from the wiki_movies_df DataFrame.
    

    # 8. Create a variable that will hold the non-null values from the “Box office” column.

    
    # 9. Convert the box office data created in Step 8 to string values using the lambda and join functions.
    

    # 10. Write a regular expression to match the six elements of "form_one" of the box office data.
   
    # 11. Write a regular expression to match the three elements of "form_two" of the box office data.
    

    # 12. Add the parse_dollars function.
    
    
        
    # 13. Clean the box office column in the wiki_movies_df DataFrame.

    
    # 14. Clean the budget column in the wiki_movies_df DataFrame.
    

    # 15. Clean the release date column in the wiki_movies_df DataFrame.
    

    # 16. Clean the running time column in the wiki_movies_df DataFrame.
    
    # Return three variables. The first is the wiki_movies_df DataFrame
    
    return wiki_movies_df, kaggle_metadata, ratings 


# In[4]:


# 17. Create the path to your file directory and variables for the three files.
file_dir = 
# The Wikipedia data
wiki_file = f'{file_dir}/wikipedia_movies.json'
# The Kaggle metadata
kaggle_file = f'{file_dir}/movies_metadata.csv'
# The MovieLens rating data.
ratings_file = f'{file_dir}/ratings.csv'


# In[5]:


# 18. Set the three variables equal to the function created in D1.
wiki_file, kaggle_file, ratings_file = extract_transform_load()


# In[6]:


# 19. Set the wiki_movies_df equal to the wiki_file variable. 
wiki_movies_df = wiki_file


# In[7]:


# 20. Check that the wiki_movies_df DataFrame looks like this. 
wiki_movies_df.head()


# In[8]:


# 21. Check that wiki_movies_df DataFrame columns are correct. 
wiki_movies_df.columns.to_list()


# In[ ]:




