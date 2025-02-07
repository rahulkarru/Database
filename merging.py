import pandas as pd

df1 = pd.read_csv('filtered_retail_data.csv')  
df2 = pd.read_csv('updated_healthcare_data.csv')  

columns_to_add = df1[['ID', 'ZipCode', 'Country', 'Income']]
# Limit both datasets to 55,500 rows
df2_limited=df2.head(55500)
df1_limited = df1.head(55500)
columns_to_add_limited = columns_to_add.head(55500)

# Reset index if necessary
df1_limited.reset_index(drop=True, inplace=True)
columns_to_add_limited.reset_index(drop=True, inplace=True)

# Add the columns to df2
df_combined = pd.concat([df2_limited, columns_to_add_limited], axis=1)
df_combined.to_csv('updated_dataset2.csv', index=False)  # Save the updated dataset