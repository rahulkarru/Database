import pandas as pd

df1 = pd.read_csv('updated_dataset2.csv')

columns_to_keep = ['Age','Gender','BloodGroup','Medical Condition','Medicines Prescribed','Test Results']
new_df1 = df1[columns_to_keep]


new_df1.to_csv('Using_health_data.csv', index=False)
df2 = pd.read_csv('updated_dataset2.csv')

columns_to_keep = ['Age','Gender','ID','ZipCode','Country','Income']
new_df2 = df2[columns_to_keep]


new_df2.to_csv('Using_Geographical_data.csv', index=False)

print("New dataset created successfully!")