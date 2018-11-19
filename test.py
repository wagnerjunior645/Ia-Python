import requests
import json

# # API Noticias https://newsapi.org/docs/get-started
# url = ('https://newsapi.org/v2/everything?'
#        'q=professor&'
#        'language=pt&'
#        'sortBy=popularity&'
#        'apiKey=a59b3dfb9d3f410f86db9bf2b505be0a')

# res = requests.get(url)

# artigos = res.json()['articles']

# for materia in artigos:
#     print(materia['author'])
#     print(materia['title'])
#     print(materia['url'])
#     print(materia['urlToImage'])

# import webhoseio

#     webhoseio.config(token="b1b86608-f5dc-41e3-89c9-5f9bbbdf0a0f")
#     query_params = {
# 	"q": "bolsonaro language:english",
# 	"ts": "1540036929845",
# 	"sort": "crawled"
#     }
#     output = webhoseio.query("filterWebContent", query_params)
#     print (output['posts'][0]['text']) # Print the text of the first post
#     print (output['posts'][0]['published']) # Print the text of the first post publication date

#     print(output)

url = "http://webhose.io/filterWebContent?token=b1b86608-f5dc-41e3-89c9-5f9bbbdf0a0f&format=json&ts=1540037188321&sort=crawled&q=bolsonaro%20language%3Aenglish"

res = requests.get(url)

materias = res.json()['posts']

for a in materias:
    print( a['thread']['url'] )
    print( a['thread']['site'] )
    print( a['thread']['title'] )
    print(a['thread']['site_type'])
    print(a['thread']['text'])
    print('---------------------_----------_----')