import pandas as pd
import requests
import json

# Load the CSV file from your computer
csv_file_path = 'tickets.csv'  # Replace with your actual file path

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Define the base API URL
base_url = "https://customizations.zowie.dev/ecommerce/tickets/"

# Create a list to store the results
data_list = []

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Extract the part of the URL from the CSV file
    api_endpoint_part = row['ticket id']

    api_url = base_url + str(api_endpoint_part)

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

        # Write the extracted fields to the list
        data_list.append([ticket_id, status])

        print(f"Data from {api_url} saved successfully")
    else:
        print(f"Failed to retrieve data from {api_url} with status code {response.status_code}")

# Convert the data into a pandas DataFrame
df_output = pd.DataFrame(data_list, columns=['ticketId', 'status'])

# Export the DataFrame to an Excel file
output_file_name = "output.xlsx"
df_output.to_excel(output_file_name, index=False)

print(f"All data has been saved to {output_file_name}")