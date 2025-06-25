import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
dff = df.groupby(' Country')
dff = dff.sum().sort_values(by = 'Deaths', ascending = False).head(10)
dff = dff.loc[:,'Deaths' ]
dff.index = ['USA', 'Brazil', 'India', 'Mexico', 'UK', "Italy", 'Peru', 'Spain', 'France', 'Tran']
print(dff)
dff.plot(kind = 'bar', figsize = (9,9))
plt.xlabel("Countries")
plt.ylabel("No of Deaths")
plt.legend()
plt.show()
