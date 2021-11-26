import pandas as pd

df = pd.DataFrame({'States':['California', 'Florida', 'Montana', 'Colorodo', 'Washington', 'Virginia'],
    'Capitals':['Sacramento', 'Tallahassee', 'Helena', 'Denver', 'Olympia', 'Richmond'],
    'Population':['508529', '193551', '32315', '619968', '52555', '227032']})

# Remove Index Column
df.to_excel('Data Science/states.xlsx', sheet_name='States', index=False)

# df.to_excel('Data Science/states.xlsx')

