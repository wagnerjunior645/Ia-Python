import requests
import json

# API Noticias https://newsapi.org/docs/get-started
url = ('https://newsapi.org/v2/everything?'
       'q=professor&'
       'language=pt&'
       'sortBy=popularity&'
       'apiKey=a59b3dfb9d3f410f86db9bf2b505be0a')

res = requests.get(url)

artigos = res.json()['articles']

for materia in artigos:
    print(materia['author'])
    print(materia['title'])
    print(materia['url'])
    print(materia['urlToImage'])