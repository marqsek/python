import pandas as pd
import requests
import csv
import json

# Load the CSV file from your computer
csv_file_path = 'tickets.csv'  # Replace with your actual file path

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Define the base API URL
base_url = "https://customizations.zowie.dev/ecommerce/tickets/"  # Replace with the actual base API URL

# Open a CSV file to save the selected two fields from the API responses
output_file_name = "output.csv"
with open(output_file_name, mode='w', newline='', encoding='utf-8') as output_file:
    csv_writer = csv.writer(output_file)

    # Write the header for the new CSV (with only two columns)
    csv_writer.writerow(['ticketId', 'status'])  # We want to extract ticketId and status

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        # Extract the part of the URL from the CSV file
        api_endpoint_part = row['ticket id']  # Replace 'column_name' with the actual column name

        # Construct the full API URL
        api_url = base_url + str(api_endpoint_part)

        # Define headers for the API request (with two headers)
        headers = {
            'X-API-KEY': 'c895a35c365541c4ac22a61d13bc388d',  # Replace with actual value
            'Accept': 'application/json',  # Expecting JSON response
        }

        # Make the GET request to the API
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            json_response = response.json()

            # Extract the two fields: 'ticketId' and 'status'
            ticket_id = json_response.get('ticketId')
            status = json_response.get('status')

            # Write the extracted fields to the CSV file
            csv_writer.writerow([ticket_id, f" {status}"])

            print(f"Data from {api_url} saved successfully")
        else:
            print(f"Failed to retrieve data from {api_url} with status code {response.status_code}")

print(f"All data has been saved to {output_file_name}")