#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[37]:


df = pd.read_csv(r"D:\DataScience Projects\amazon_prime_titles.csv")


# # Data Preprocessing

# # Head

# In[38]:


# head - head is used to show the top 5 elements by default 
# but we are able to define the nuumber are rows to show
df.head(2) 


# # Tail

# In[39]:


#.tail() - is used  to show the last rows
df.tail(2)


# # Shape

# In[40]:


# shape - shows the number of rows and columns in the data set
df.shape


# # Columns

# In[41]:


# Columns - is used for knowing the columns of the data set
df.columns


# # dtypes

# In[42]:


#.dtypes - used to know the datatype of each column
df.dtypes


# # unique
# In a column, It shows the unique value of specific column

# In[43]:


df["director"].unique()


# # nunique
# It will show the total number of unique value from whole data frame

# In[44]:


df.nunique()


# # describe
# describe() is used to showcase the mean, standarad deviation , count etc...

# In[45]:


df.describe()


#  # .value_counts
#  It shows all the unique values with their count
# 

# In[46]:


df["director"].value_counts()


# # isnull 
# it shows the null values

# In[47]:


df.isnull()


# # Task 1
# # How many Null Value present , Show all the null values using heatmap

# In[50]:


sns.heatmap(df.isnull())


# # Task 2
# # In which Year Highest Number of TV shows and movies were released

# In[51]:


df['release_year'].value_counts()


# # Task 3
# # How many Movies and Tv shows are in tthe dataset

# In[52]:


df.type.value_counts()


# In[53]:


df['type'].value_counts()


# In[67]:


movie_keys = list(df[df['type'] == 'Movie'].type)
tv_keys = list(df[df['type'] == 'TV Show'].type)


# In[70]:


df.type.value_counts().plot(kind = 'pie')


# In[71]:


df.type.value_counts().plot(kind = 'bar')


# # Task 4 :
# # show all the records with type "movies" & country is "United Kingdom"

# In[74]:


df[(df["type"] == 'Movie') & (df["country"] == "United Kingdom")].head(3)


# # Task 5
# # Show top 3 irectors . who gave the highest numbeer of tv shows and movies released on prime video

# In[77]:


df["director"].value_counts().head(3)


# In[ ]:





# In[ ]:




