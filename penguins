import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
penguins = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-28/penguins.csv')
penguins = penguins.dropna()

fig, axs = plt.subplots(2, 2, sharex=True, figsize=(9, 7))
fig.suptitle('Physical Characteristics of Three Penguin Species', y=1.05, fontsize=20, fontweight='bold')

sns.violinplot(ax=axs[0, 0], x=penguins['species'], y=penguins['bill_length_mm'])
axs[0, 0].set_ylabel('Bill length (in millimeters)', fontweight='bold')

sns.violinplot(ax=axs[0, 1], x=penguins['species'], y=penguins['bill_depth_mm'])
axs[0, 1].yaxis.tick_right()
axs[0, 1].yaxis.set_label_position("right")
axs[0, 1].set_ylabel('Bill depth (in millimeters)', fontweight='bold')

sns.violinplot(ax=axs[1, 0], x=penguins['species'], y=penguins['flipper_length_mm'])
axs[1, 0].set_ylabel('Flipper length (in millimeters)', fontweight='bold')

sns.violinplot(ax=axs[1, 1], x=penguins['species'], y=penguins['body_mass_g'])
axs[1, 1].yaxis.tick_right()
axs[1, 1].yaxis.set_label_position("right")
axs[1, 1].set_ylabel('Body mass (in grams)', fontweight='bold')

for ax in axs.flat:
    ax.set_xlabel('')
    
fig.tight_layout()
plt.show()
