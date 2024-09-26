import pandas as pd
import requests
import json

source_file = 'tickets.csv'

df = pd.read_csv(source_file)

main_url = "https://customizations.zowie.dev/ecommerce/tickets/"

data_list = []

for index, row in df.iterrows():
    endpoint_url = row['ticket id']
    api_url = main_url + str(endpoint_url)

    headers = {
        'X-API-KEY': 'c895a35c365541c4ac22a61d13bc388d',
        'Accept': 'application/json',
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        json_response = response.json()

        ticket_id = json_response.get('ticketId')
        status = json_response.get('status').strip()

        data_list.append([ticket_id, status])

        print(f"Data saved successfully")
    else:
        print(f"Failed to retrieve data with status code {response.status_code}")

df_output = pd.DataFrame(data_list, columns=['ticketId', 'status'])

output_file_name = "output.xlsx"
with pd.ExcelWriter(output_file_name, engine='xlsxwriter') as writer:
    df_output.to_excel(writer, sheet_name='Sheet1', index=False)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    worksheet.write_formula('D2', '=UNIQUE(B2:B54)')

    for row in range(2, 5):
        worksheet.write_formula(f'E{row}', f'=COUNTIF(B2:B10001, D{row})')

print(f"All data has been saved to {output_file_name}")
