# place your code to clean up the data file below.
import requests
import pandas
import json

url = "https://data.cityofnewyork.us/resource/k397-673e.json?$limit=5000"
response = requests.get(url)
data = json.loads(response.content)
df = pandas.json_normalize(data)
df.to_csv("data/Original_data_file.csv")

#clean out unnecessary columns in the dataset
import pandas as pd
df2 = pd.read_csv("data/original_data_file.csv")

# Display the DataFrame before deleting the column
print("Before deleting column:")
print(df2.head())

# Use drop() function to delete the unwanted columns
column_to_delete = ['payroll_number','last_name','first_name','mid_init','agency_start_date','agency_name','leave_status_as_of_june_30','title_description']
df2.drop(column_to_delete, axis=1, inplace=True)

# Display the DataFrame after deleting the column
print("\nAfter deleting column:")
print(df2.head())

#drop unwanted rows
df2.drop(df2[df2['pay_basis'] != 'per Annum'].index, axis=0, inplace=True)

# Save the modified DataFrame back to a CSV file
df2.to_csv('data/Clean_data.csv', index=False)