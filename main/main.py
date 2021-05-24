import requests
import config
from PIL import Image  # Dependency for WordCloud
from wordcloud import WordCloud

url = 'https://api.groupme.com/v3/groups/62449433/messages'  # IS 4420 Systems Analysis Group
params = {'token': config.access_token, 'limit': 100, 'before_id': '160705055250796165'}

r = requests.get(url, params=params)

while r.status_code != 304:
    json_data = r.json()
    conversationText = [str(item['text']) for item in json_data['response']['messages']]
    max_index = len(json_data['response']['messages'])
    params['before_id'] = json_data['response']['messages'][max_index-1]['id']
    r = requests.get(url, params=params)

wordCloud = WordCloud().generate(str(conversationText))

wordCloud.to_file("img/firstCloud.png")
