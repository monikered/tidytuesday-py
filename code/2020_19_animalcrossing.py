# load the villager data and modules

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

villagers = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv', 
                        usecols=['name', 'gender', 'species','personality'])

# view the villagers by gender, then calculate and sort by proportion male per species
animals = villagers.groupby(['species', 'gender']).size().unstack('gender').fillna(0)
animals['proportion_m'] = round(animals['male']/(animals['male'] + animals['female']),2)
animals = animals.sort_values('proportion_m', ascending=False)

# set x and y
x = animals.index
y = animals['male'] + animals['female']
# using a divergent color scale to show distance from 50/50 parity
data_color =  animals['proportion_m']
data_color = [x / max(data_color) for x in data_color]
my_cmap = plt.cm.get_cmap('PiYG')
colors = my_cmap(data_color)

fig, ax = plt.subplots(1, 1, figsize=(12, 7))
ax.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
plt.bar(x, y, color=colors, edgecolor='black')
plt.xticks(rotation=70)
plt.title('Gender ratios of Animal Crossing villagers, by species', fontname='Giddyup Std', fontsize='32')
plt.ylabel('Count', fontname='Giddyup Std', fontsize='20')
# add annotations to the plot
ann = ax.annotate('Goats, monkeys, rhinos, and (bear) cubs are at gender parity!', 
                  xytext=('deer',21), 
                  bbox=dict(boxstyle='round', fc='w'),
                  xy=('goat',8.5), 
                  arrowprops=dict(arrowstyle='->', 
                                  connectionstyle='arc3, rad=-0.2')
                  )
ann = ax.annotate('', 
                  xytext=('pig',20.5), xy=('cub',16.5), 
                  arrowprops=dict(arrowstyle='->', 
                                  connectionstyle='arc3, rad=-0.2')
                  )
ann = ax.annotate('All bulls and all\n lions are male',
                  xytext=('bull',19), xy=('bull',6.5),
                  bbox=dict(boxstyle='round', fc='w'),
                  arrowprops=dict(arrowstyle='->',
                                  connectionstyle='arc3, rad=0.2')
                  )
ann = ax.annotate('Cows are \n100% female',
                  xytext=('kangaroo',18), xy=('cow',4.5),
                  bbox=dict(boxstyle='round', fc='w'),
                  arrowprops=dict(arrowstyle='->',
                                  connectionstyle='arc3, rad=-0.2')
                  )
                  
# plot the colorbar legend
sm = ScalarMappable(cmap=my_cmap.reversed(), norm=plt.Normalize(0,max(data_color)))
sm.set_array([])
cbar = plt.colorbar(sm, orientation='horizontal', shrink=0.91, pad=0.15)
cbar.set_label('100% male...                                                                                                                                                  ...to 100% female',labelpad=5)
cbar.ax.get_xaxis().set_ticks([])

plt.show()
