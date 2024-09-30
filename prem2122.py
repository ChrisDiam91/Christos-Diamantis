import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv(r"C:\Users\CHRISTOSMAR\OneDrive\Υπολογιστής\Data\Premier21-22.csv")

# Plot Home and Away Goals vs xGoals with a reference line

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Home Goals vs Home xGoals
sns.scatterplot(x='Home xG', y='Home GF', hue='Squad', data=data, s=100, ax=axes[0])
axes[0].plot([data['Home xG'].min(), data['Home xG'].max()],
             [data['Home GF'].min(), data['Home GF'].max()],
             'r--', label='xGoals = Goals')
axes[0].set_title('Home Goals vs Home xGoals (2021-2022)')
axes[0].set_xlabel('Home xGoals')
axes[0].set_ylabel('Home Goals')
axes[0].grid(True)
axes[0].legend(bbox_to_anchor=(1.05, 1),loc='upper left',title='Team')

# Away Goals vs Away xGoals
sns.scatterplot(x='Away xG', y='Away GF', hue='Squad', data=data, s=100, ax=axes[1])
axes[1].plot([data['Away xG'].min(), data['Away xG'].max()],
             [data['Away GF'].min(), data['Away GF'].max()],
             'r--', label='xGoals = Goals')
axes[1].set_title('Away Goals vs Away xGoals (2021-2022)')
axes[1].set_xlabel('Away xGoals')
axes[1].set_ylabel('Away Goals')
axes[1].grid(True)
axes[1].legend(bbox_to_anchor=(1.05, 1),loc='upper left',title='Team')

# Adjust layout
plt.tight_layout()
plt.show()


