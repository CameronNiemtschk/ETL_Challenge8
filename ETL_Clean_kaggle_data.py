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


# In[2]:


#  Add the clean movie function that takes in the argument, "movie".
def clean_movie(movie):
        wiki_movies_df =  pd.read_csv('movies_metadata.csv')
    kaggle_metadata = pd.read_csv('ratings.csv')
    with open ('wikipedia-movies.json', mode='r') as file:
        ratings = pd.DataFrame(json.load(file))
    return wiki_movies_df, kaggle_metadata, ratings
    

    return movie


# In[3]:


# 1 Add the function that takes in three arguments;
# Wikipedia data, Kaggle metadata, and MovieLens rating data (from Kaggle)

def function_name():
    # Read in the kaggle metadata and MovieLens ratings CSV files as Pandas DataFrames.
    

    # Open and read the Wikipedia data JSON file.
    
    
    # Write a list comprehension to filter out TV shows.
    

    # Write a list comprehension to iterate through the cleaned wiki movies list
    # and call the clean_movie function on each movie.
    

    # Read in the cleaned movies list from Step 4 as a DataFrame.


    # Write a try-except block to catch errors while extracting the IMDb ID using a regular expression string and
    #  dropping any imdb_id duplicates. If there is an error, capture and print the exception.
    try:
        
    except 

    #  Write a list comprehension to keep the columns that don't have null values from the wiki_movies_df DataFrame.
    

    # Create a variable that will hold the non-null values from the “Box office” column.

    
    # Convert the box office data created in Step 8 to string values using the lambda and join functions.
    

    # Write a regular expression to match the six elements of "form_one" of the box office data.
   
    # Write a regular expression to match the three elements of "form_two" of the box office data.
    

    # Add the parse_dollars function.
    
        
    # Clean the box office column in the wiki_movies_df DataFrame.

    
    # Clean the budget column in the wiki_movies_df DataFrame.
    

    # Clean the release date column in the wiki_movies_df DataFrame.
    

    # Clean the running time column in the wiki_movies_df DataFrame.
    
     
    # 2. Clean the Kaggle metadata.

    # 3. Merged the two DataFrames into the movies DataFrame.


    # 4. Drop unnecessary columns from the merged DataFrame.


    # 5. Add in the function to fill in the missing Kaggle data.


    # 6. Call the function in Step 5 with the DataFrame and columns as the arguments.


    # 7. Filter the movies DataFrame for specific columns.


    # 8. Rename the columns in the movies DataFrame.


    # 9. Transform and merge the ratings DataFrame.
    
    return wiki_movies_df, movies_with_ratings_df, movies_df


# In[4]:


# 10. Create the path to your file directory and variables for the three files.
file_dir = '../Resources'
# The Wikipedia data
wiki_file = f'{file_dir}/wikipedia_movies.json'
# The Kaggle metadata
kaggle_file = f'{file_dir}/movies_metadata.csv'
# The MovieLens rating data.
ratings_file = f'{file_dir}/ratings.csv'


# In[5]:


# 11. Set the three variables equal to the function created in D1.
wiki_file, kaggle_file, ratings_file = extract_transform_load()


# In[6]:


# 12. Set the DataFrames from the return statement equal to the file names in Step 11. 
wiki_movies_df = wiki_file
movies_with_ratings_df = kaggle_file
movies_df = ratings_file


# In[7]:


# 13. Check the wiki_movies_df DataFrame. 
wiki_movies_df.head()


# In[8]:


# 14. Check the movies_with_ratings_df DataFrame.
movies_with_ratings_df.head()


# In[9]:


# 15. Check the movies_df DataFrame. 
movies_df.head()


# In[ ]:




