import requests
import csv
from io import StringIO

url = 'https://customizations.zowie.dev/ecommerce/tickets/1127762561'
headers = {
    'X-API-KEY': 'c895a35c365541c4ac22a61d13bc388d',
    'Accept': 'text/csv',  # Requesting CSV response
    'Content-Type': 'application/json'
}

response = requests.request("GET", url,headers=headers,data={})
myjson = response.json()
ourdata=[]
csvheader = ['ticketId','status']

for x in myjson['data']:
    listing = [x['ticketId'],x['status']]
    ourdata.append(listing)

with open('ticksy.csv','w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)

print(done)
print(response.json())