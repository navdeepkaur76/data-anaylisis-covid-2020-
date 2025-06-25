import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
dff = df.set_index(' Country')
case = []
for index, row in dff.iterrows():
    if index == 'India':
        case.append(row['Cases'])
days = list(range(1, 279))
plt.plot(days, case)
plt.title ('INDIA')
plt.xlabel('No of Days')
plt.ylabel("No of Cases")
plt.show()
