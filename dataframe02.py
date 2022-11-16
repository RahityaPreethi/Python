import pandas as pd
data = {'country':['Belgium','India','Brazil'],
'capital':['Brussels','Delhi','Brasilia'],
'population':[11190846,1303171035,207847528]}

df = pd.DataFrame(data,columns=['country','capital','population'])

print(df)