import pandas as pd
import matplotlib.pyplot as plt
#Report and Plot Number of cases and death in different region
df = pd.read_csv('data.csv')
df = df.pivot_table(index = 'Region', aggfunc= 'sum')
df = df.loc[:, 'Cases':'Deaths']
print(df)
df. plot()
plt.show()
