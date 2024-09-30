import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data22 = pd.read_csv(r"C:\Users\CHRISTOSMAR\OneDrive\Υπολογιστής\Data\Premier22_23.csv")

fig, axes = plt.subplots(1,2,figsize= (16,6))

#Home Goals vs Home xGoals
sns.scatterplot(x='Home GF', y='Home xG', data=data22, color='red',s=100, hue='Squad', ax=axes[0])
axes[0].plot([data22['Home xG'].min(), data22['Home xG'].max()],
             [data22['Home GF'].min(), data22['Home GF'].max()],
             'r--', label='xGoals = Goals')
axes[0].set_title('Home Goals vs Home xGoals (2022-2023)')
axes[0].set_xlabel('Home xGoals')
axes[0].set_ylabel('Home Goals')
axes[0].grid(True)
axes[0].legend(bbox_to_anchor=(1.05, 1),loc='upper left',title='Team')

#Away goals vs Away XGoals
sns.scatterplot(x='Away GF', y='Away xG', data=data22, color='magenta',s=100, hue='Squad', ax=axes[1])
axes[1].plot([data22['Away xG'].min(), data22['Away xG'].max()],
             [data22['Away GF'].min(), data22['Away GF'].max()],
             'r--', label='xGoals = Goals')
axes[1].set_title('Away Goals vs Away xGoals (2022-2023)')
axes[1].set_xlabel('Away xGoals')
axes[1].set_ylabel('Away Goals')
axes[1].grid(True)
axes[1].legend(bbox_to_anchor=(1.05, 1),loc='upper left',title='Team')

# Adjust layout
plt.tight_layout()
plt.show()