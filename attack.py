import pandas as pd

df_medical = pd.read_csv('merged_dataset.csv')
df_demographic = pd.read_csv('Using_Geographical_data.csv')


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
    print(reidentified_data.sample(10))  
else:
    print("No matches found.")