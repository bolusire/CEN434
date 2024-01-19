import pandas as pd
import numpy as np

a = [1, 7, 2]
myvar = pd.Series(a)

#print(myvar)
#print(myvar[0])

import pandas as pd

data = {
  "x": [1,2,3,4,5], "y": [2,4,6,8,10]
     }

#load data into a DataFrame object:

df = pd.DataFrame(data)

#df

print(df.loc[0])
df_new = pd.read_excel(r"C:\Users\donke\OneDrive\Documents\Python\array.xlsx")
print(df_new)
a = df.to_numpy()

#print(a)