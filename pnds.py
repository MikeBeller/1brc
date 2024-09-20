import pandas as pd
r=(pd.read_csv('data/measurements.100m.txt',sep=';',
               names=['sta','val'],
               dtype={'sta':str,'val':float},
               index_col=False)
   .groupby('sta')
   .val.agg(['mean','min','max'])
   .collect())
    
print(r)
