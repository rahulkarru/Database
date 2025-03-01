import pandas as pd
import matplotlib.pyplot as plt


import numpy as np


df_medical = pd.read_csv("merged_dataset.csv") 
df_demographic = pd.read_csv("Using_Geographical_data.csv") 

print("Medical Dataset:")
print(df_medical.head())
print("\nDemographic Dataset:")
print(df_demographic.head())


required_columns = ['Age', 'Gender', 'ZipCode']
for col in required_columns:
    if col not in df_medical.columns:
        raise ValueError(f"Column '{col}' not found in medical dataset.")
    if col not in df_demographic.columns:
        raise ValueError(f"Column '{col}' not found in demographic dataset.")

df_medical['Age'] = df_medical['Age'].fillna('Unknown')
df_medical['Gender'] = df_medical['Gender'].fillna('Unknown')
df_medical['ZipCode'] = df_medical['ZipCode'].fillna('Unknown')

df_demographic['Age'] = df_demographic['Age'].fillna('Unknown')
df_demographic['Gender'] = df_demographic['Gender'].fillna('Unknown')
df_demographic['ZipCode'] = df_demographic['ZipCode'].fillna('Unknown')


df_medical['Composite_Key'] = df_medical['Age'].astype(str) + '_' + df_medical['Gender'].astype(str) + '_' + df_medical['ZipCode'].astype(str)
df_demographic['Composite_Key'] = df_demographic['Age'].astype(str) + '_' + df_demographic['Gender'].astype(str) + '_' + df_demographic['ZipCode'].astype(str)


reidentified_data = pd.merge(df_medical, df_demographic, on='Composite_Key', how='inner')

print(f'\nNumber of re-identified matches: {len(reidentified_data)}')
if len(reidentified_data) > 0:
    print('\nSample of re-identified records:')
    print(reidentified_data.sample(min(10, len(reidentified_data))))  
else:
    print("No matches found.")


plt.figure(figsize=(8, 5))
bars = plt.bar(["Total Records", "Matched Records"], [len(df_medical), len(reidentified_data)], color=['blue', 'red'])
plt.xlabel("Category")
plt.ylabel("Number of Records")
plt.title("Total vs. Matched Records")


for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.show()

