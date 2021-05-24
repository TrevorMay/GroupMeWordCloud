import requests
import config
from PIL import Image  # Dependency for WordCloud
from wordcloud import WordCloud

url = 'https://api.groupme.com/v3/groups/60111703/messages'  # IS 4420 Systems Analysis Group
params = {'token': config.access_token, 'limit': 100}

# Get one page of data, pull off messages and index of last message for next page
r = requests.get(url, params=params)
json_data = r.json()
message_list = [item['text'] for item in json_data['response']['messages']]
max_index = len(json_data['response']['messages'])
params['before_id'] = json_data['response']['messages'][max_index-1]['id']
i = 1

# keep paging back to beginning
while r.status_code == 200:
    r = requests.get(url, params=params)
    if r.status_code == 200:
        json_data = r.json()
        message_list += [item['text'] for item in json_data['response']['messages']]
        max_index = len(json_data['response']['messages'])
        params['before_id'] = json_data['response']['messages'][max_index-1]['id']
        print(i)
        i += 1
        continue
    else:
        continue

# filter out None messages, probably images
filtered_text = list(filter(None, message_list))
# Turn into one long string to feed into WordCloud
entire_string = ' '.join(filtered_text)

# Write string to a txt file so we don't have to repeat calls all the time
with open('ISText.txt', 'w', encoding='utf-8') as text_file:
    print(entire_string, file=text_file)

