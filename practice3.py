import pandas as pd
print('Df with Lists')
day=['Mon','Tue','Wed','Thu','Fri','Sat']
month=['Jan','Feb','Mar','Apr','May','Jun']
df=pd.DataFrame(day,month)
print(df)
print('List of Dict')
d={'Month':month,
   'Days':[31,28,31,30,31,30]}
dff=pd.DataFrame(d)
print(dff)
