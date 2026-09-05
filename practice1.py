import pandas as pd
data={'Name':['Alice','Charlie','Peter'],
       'Class':['XII','XI','X']}
df=pd.DataFrame(data)
df['Age']=[12,13,13]
print(df)
