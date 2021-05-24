from PIL import Image  # Dependency for WordCloud
from wordcloud import WordCloud

# Some word dominate the cloud we don't want those
boring_words = {'going', 'yeah', 'it', 'and', 'that', 'I', 'you', 'for', 'the', 'we', 'me', 'just', 'to', 'on', 'a',
                'do', 'be', 'in', 'is', 'is', 'so', 'have', 'this', 'but', 'are', 'when', 'get', 'no', 'not', 'can',
                'have', 'also', 'what', 'my', 'like', 'at', 'with', 'there', 'if', "I'm", 'was', 'your', 'of', 's', 'm',
                'from', 'all', 'out', 'they', 'guy', 'she', 'think', 'or', 'up', 'he', 'one', 'u', 'guys', 'go', 'here',
                'am', 'need', "don't", "because", 'did', 'then', 'about'}

with open('ISText.txt', 'r', encoding='utf-8') as text_file:
    wordCloud = WordCloud(
        width=1000,
        height=1000,
        max_words=400,
        stopwords=boring_words)\
        .generate(text_file.read())

    wordCloud.to_file("img/ISCloud3.png")
