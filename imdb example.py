# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:11:40 2020

@author: admin1
"""

import pandas as pd
import matplotlib.pyplot as plt
movies_df = pd.read_csv("imdb_1000.csv", index_col="star_rating")
#print (movies_df.head(10))
#print (movies_df.tail(10))
#print (movies_df['genre'].value_counts())
#subset = movies_df[['title','genre']]
#print(subset.head(10))
#movies_df = pd.read_csv("imdb_1000.csv", index_col="title")
#inc = movies_df.loc["Inception"]
#print(inc)
#movies_df.plot( x='title', y='duration')