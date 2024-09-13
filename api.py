import requests

response=requests.get('https://randomuser.me/api')
print(response.status_code) #prints response status code
print(response.json()) # prints whole content

gender = response.json()['results'][0]['gender'] #creating variable to specify conditions of printed results
print(gender)

title = response.json()['results'][0]['name']['title']
first_name = response.json()['results'][0]['name']['first']
last_name = response.json()['results'][0]['name']['last']
print(last_name)

print(f'{title}. {first_name} {last_name}')