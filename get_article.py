# CREDIT: based on the work of Charles Nadeau at
# https://help.zendesk.com/hc/en-us/articles/229136947

import json
import requests
import os

# Target a Zendesk subdomain (subdomain.zendesk.com)
subdomain = '<subdomain>'

# Identify the article to retrieve with its Zendesk unique id
articleID = '<articleID>'

# Provide authentication credentials for the subdomain
user = '<user>/token'
pwd = '<api-token>'

# Set the input/output directory for text files (JSON objects)
outputRoot = '<c:\\path\\>'
outputFolder = outputRoot + subdomain + '\\articles\\'

# Set the request parameters
apiEndPoint = '/api/v2/help_center/en-us/articles/' + articleID + 'json'
url = 'https://' + subdomain + '.zendesk.com' + apiEndPoint
headers = {'content-type': 'application/json'}

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
  print('Status:', response.status_code, 'Problem with the request. Exiting.')
  exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()

# Loop through the article dictionary
article = data['article']
# Purge keys from the dictionary that aren't needed re-recreate the article
del (article['id'],
     article['draft'],
     article['promoted'],
     article['vote_sum'],
     article['vote_count'],
     article['url'],
     article['html_url'],
     article['author_id'],
     article['comments_disabled'])
    
# Save article as a JSON object in a text file
outputFile = outputFolder + article['name'] + '.txt'
if not os.path.exists(outputFolder):
  os.makedirs(outputFolder)
with open(outputFile, mode='w', encoding='utf-8') as f:
  json.dump((article), f, ensure_ascii=True, indent=2)
  # Show article output
  print('Saved article ' + article['name'])
