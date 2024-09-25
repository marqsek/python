import pandas as pd
import requests
import csv
from io import StringIO

# Load the CSV file from your computer
csv_file_path = 'tickets.csv'  # Replace with your actual file path

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Define the base API URL
base_url = "https://customizations.zowie.dev/ecommerce/tickets/"  # Replace with the actual base API URL

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Extract the part of the URL from the CSV file
    api_endpoint_part = row['ticket id']  # Replace 'column_name' with the actual column name

    # Construct the full API URL
    api_url = base_url + str(api_endpoint_part)

    # Prepare headers for the API request
    headers = {
        'X-API-KEY': 'c895a35c365541c4ac22a61d13bc388d',  # Replace with your actual API key
        'Accept': 'text/csv',  # Requesting CSV response
    }

    # Make the GET request to the API
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Process the CSV response
        csv_content = response.text
        csv_reader = csv.reader(StringIO(csv_content))

        # Save the API CSV response to a new CSV file
        output_file_name = f"output_{index}.csv"  # Each response will be saved as a separate file
        with open(output_file_name, mode='w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)

            # Write each row of the CSV response to the output file
            for csv_row in csv_reader:
                csv_writer.writerow(csv_row)

        print(f"CSV data saved to {output_file_name}")
    else:
        print(f"Failed to retrieve data from {api_url} with status code {response.status_code}")
