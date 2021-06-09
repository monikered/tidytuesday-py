#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 22:05:04 2020

@author: monicaremmers
"""

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_cloud(wordcloud, save_as):
    plt.figure(figsize=(30, 20))
    plt.imshow(wordcloud) 
    plt.axis("off")
    plt.savefig(save_as);

chopped = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-08-25/chopped.tsv', sep='\t', header=0)
df = chopped[['series_episode', 'appetizer', 'entree', 'dessert']]
filenames = ['apps_wc.png', 'entr_wc.png', 'dess_wc.png']
courses = ['appetizer', 'entree', 'dessert']
    
for i, course in zip(range(3), courses):
    ingredients = ', '.join([str(elem) for elem in df[course].tolist()])
    cloud = WordCloud(width=900, height=600, max_words=250, min_font_size=6,
                      background_color='white', color_func=lambda *args, **kwargs: "black", 
                      relative_scaling=1, collocations=False).generate(ingredients)
    plot_cloud(cloud, filenames[i]) 
