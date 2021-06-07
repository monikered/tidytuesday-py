#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:04:20 2020

@author: monicaremmers
"""

import pandas as pd
import numpy as np

chopped = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-08-25/chopped.tsv', sep='\t', header=0)

df = chopped[['series_episode', 'appetizer', 'entree', 'dessert']]
df = df[df['appetizer'].notnull()] # tbh I forgot what this does but when I try to change it the code breaks


def prep_ingredients(course, course_variable):
    course = pd.concat([pd.Series(row['series_episode'], row[course_variable].split(', '))              
                for index, row in df.iterrows()]).reset_index()
    course.columns = ['ingredient', 'episode number']
    course['round'] = course_variable
    return course

#create  ingredient lists for each course
columns = ['ingredient', 'episode number', 'round']
apps = prep_ingredients(pd.DataFrame(columns=columns), 'appetizer')
entr = prep_ingredients(pd.DataFrame(columns=columns), 'entree')
dess = prep_ingredients(pd.DataFrame(columns=columns), 'dessert')

# all the ingredients together
ingredients = pd.concat([apps, entr, dess])
ingredients.sort_values(by=['ingredient', 'episode number'], inplace=True)


freq = ingredients.apply(pd.value_counts)
freq = freq.sort_values(by=['ingredient'], inplace=False)

# TODO: remove all phrases in parentheses from the ingredients
# Questions worth asking: what words (or ingredients) most DISTINGUISH one course from another? UserWarning(1) TF-IDF to find out
