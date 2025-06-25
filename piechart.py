import pandas as pd
import matplotlib.pyplot as plt
#Report and Plot of Top five Countries According to Cases
df = pd.read_csv("data.csv")
dff = df.groupby(' Country' )
dff = dff.sum().sort_values(by = 'Cases', ascending = False).head(5)
print(dff)
dff = dff. loc[:, 'Cases' ]
print(dff)
dff.plot(kind = 'pie', y = 'Cases', labels = dff.index, startangle = 90, explode = (0.05, 0,0,0,0))
plt.legend()
plt.title("TOP 5 Countries")
plt.show()
