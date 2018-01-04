import json
import requests
import os

# Target a Zendesk subdomain (subdomain.zendesk.com)
subdomain = '<subdomain>'

# Provide authentication credentials for the subdomain
user = '<user>/token'
pwd = '<api-token>'

# Set the input/output directory for text files (JSON objects)
outputRoot = 'c:\\<path>\\'
outputFolder = outputRoot + subdomain + '\\sections\\'

# Set the request parameters
apiEndPoint = '/api/v2/help_center/en-us/sections.json'
url = 'https://' + subdomain + '.zendesk.com' + apiEndPoint
headers = {'content-type': 'application/json'}

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
  print('Status:', response.status_code, response.text)
  exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()

# Loop through the sections dictionary
section_list = data['sections']
for section in section_list:
    # Purge keys from the object not required by the API for POST
    del (section['id'],
         section['source_locale'],
         section['url'],
         section['html_url'],
         section['outdated'],
         section['created_at'],
         section['updated_at'],
         section['category_id'],
         section['user_segment_id'])
    
    # Create a folder for the output and name the file
    if not os.path.exists(outputFolder):
      os.makedirs(outputFolder)
    sectionName = section['name'] + '.txt'
    outputFile = outputFolder + sectionName

    # Wrap each section object in a parent "section" object.
    # The API requires this to POST sections back to the HC.
    section = {"section": section}

    # Save the file
    with open(outputFile, mode='w', encoding='utf-8') as f:
      json.dump((section), f, ensure_ascii=True, indent=2)

    # Show section output
    print('Saved section ' + sectionName)
