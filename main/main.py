import requests
import config
from PIL import Image  # Dependency for WordCloud
from wordcloud import WordCloud

url = 'https://api.groupme.com/v3/groups/62449433/messages'  # IS 4420 Systems Analysis Group
params = {'token': config.access_token, 'limit': 100, 'before_id': '160705055250796165'}

r = requests.get(url, params=params)

json_data = r.json()

conversationText = ''

for item in json_data['response']['messages']:
    conversationText += str(item['text'])

wordCloud = WordCloud().generate(conversationText)

wordCloud.to_file("img/firstCloud.png")
