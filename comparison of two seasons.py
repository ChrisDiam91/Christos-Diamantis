import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

season_21_22 = pd.read_csv(r"C:\Users\CHRISTOSMAR\OneDrive\Υπολογιστής\Data\Premier21-22.csv")
season_22_23 = pd.read_csv(r"C:\Users\CHRISTOSMAR\OneDrive\Υπολογιστής\Data\Premier22_23.csv")

season_21_22['Season'] = '2021-2022'
season_22_23['Season'] = '2022-2023'
data = pd.concat([season_21_22, season_22_23])

# Add Total Goals and Total xGoals for both home and away matches
data['Total Goals'] = data['Home GF'] + data['Away GF']
data['Total xGoals'] = data['Home xG'] + data['Away xG']

# Now we have data for both seasons, let's plot them for comparison
# Plot Goals vs xGoals for each season
plt.figure(figsize=(12, 7))
sns.scatterplot(x='Total xGoals', y='Total Goals', hue='Season', style='Squad', data=data, s=100)

#annotation for each squad
for i in range(len(data)):
    plt.annotate(data['Squad'].iloc[i],
                 (data['Total xGoals'].iloc[i], data['Total Goals'].iloc[i]),
                 textcoords="offset points",
                 xytext=(5, 5), ha='center')

# Customize the plot
plt.title('Actual Goals vs Expected Goals Comparison for 2021-2022 and 2022-2023 Seasons')
plt.xlabel('Total xGoals')
plt.ylabel('Total Goals')
plt.grid(True)
plt.legend(title='Season', loc='best', labels=data['Season'].unique())
# Show plot
plt.show()


