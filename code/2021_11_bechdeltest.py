#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:55:09 2021

@author: monicaremmers
"""

import pandas as pd
import re


movies = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-03-09/movies.csv', error_bad_lines=False)

# clean up names of films in dataset
def Clean_names(title):    
    title = re.sub('&amp;', '&', title)
    title = re.sub('&#39;', '\'', title)
    title = re.sub('&uuml;', 'ü', title)
    title = re.sub('&agrave;', 'à', title)
    return title

movies['title'] = movies['title'].apply(Clean_names)

# Which directors have the most films on this list?
directors = movies.groupby('director').count().reset_index()

# MPAA ratings and bechdel test