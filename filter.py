import csv

input_filename = 'healthcare_prediction_dataset.csv'
output_filename = 'updated_healthcare_data.csv'


columns_to_keep = [0,1, 2, 3, 4, 13, 14]

column_headings = ['Name', 'Age', 'Gender', 'BloodGroup', 'Medical Condition', 'Medicines Prescribed', 'Test Results']


with open(input_filename, 'rt') as infile:
    reader = csv.reader(infile, delimiter=',')
    
    # Open the output CSV file for writing
    with open(output_filename, 'wt', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write the header to the output file
        writer.writerow(column_headings)
        
        # Iterate through each row in the input CSV
        for row in reader:
            # Check if the row has enough columns to avoid IndexError
            if len(row) > max(columns_to_keep):  # Ensure there are enough columns
                # Filter the desired columns
                filtered_row = [row[i] for i in columns_to_keep]
                # Write the filtered row to the output file
                writer.writerow(filtered_row)

print(f"Filtered data has been saved to {output_filename}.")