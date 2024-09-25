import requests
from requests.auth import HTTPBasicAuth
import csv

api_token = 'c895a35c365541c4ac22a61d13bc388d'
headers = {
    'Accept': 'application/json',
    'Content-type': 'application/json'
    'X-Authentication-Token : api_token'
}

url_base = 'https://customizations.zowie.dev/ecommerce/tickets/14105879614'
response = requests.request("GET", url_base,headers=headers,data={})
myjson = response.json()
ourdata=[]
csvheader = ['ticketId','status']

for x in myjson['data']:
    listing = [x['ticketId'],x['status']]
    ourdata.append(listing)

with open('new_tickets.csv','w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)


print('done')
