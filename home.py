import urllib3.request
import requests
import keys

# get all available memes
data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
images = [{'name': image['name'], 'url': image['url'], 'id': image['id']} for image in data]

# list all available memes
counter = 1
for img in images:
    print(counter, img['name'])
    counter = counter + 1

# take user input
id = int(input('Enter the meme serial number (e.g. 1, 2..) : '))
text0 = input('Enter first text : ')
text1 = input('Enter second text : ')

# Lets get the generated meme
URL = 'https://api.imgflip.com/caption_image'
params = {
    'username': keys.username,
    'password': keys.password,
    'template_id': images[id-1]['id'],
    'text0': text0,
    'text1': text1
}

response = requests.request('POST', URL, params=params).json()
print(response)

# Save meme

opener = urllib3.request
opener.addheader('User-Agent', keys.userAgent)
filename, headers = opener.retrieve(response['data']['url'], images[id-1]['name']+'.jpg')