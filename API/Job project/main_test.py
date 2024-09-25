import requests
import csv
from io import StringIO

url_base = 'https://customizations.zowie.dev/ecommerce/tickets/'
request_url = url_base + '1127762561'
#api_token = 'c895a35c365541c4ac22a61d13bc388d'
headers = {
    'X-API-KEY' : 'c895a35c365541c4ac22a61d13bc388d',
    'Accept': 'text/csv',
    'Content-type': 'application/json'
}

response = requests.get(request_url,headers=headers)

if response.status_code == 200:
    # Process the CSV content
    csv_content = response.text
    csv_reader = csv.reader(StringIO(csv_content))

    # Save the CSV content to a file
    with open('../output.csv', mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)

        # Write each row of the CSV
        for row in csv_reader:
            csv_writer.writerow(row)

    print("CSV data saved to output.csv")
else:
    print(f"Failed to retrieve data: {response.status_code}")