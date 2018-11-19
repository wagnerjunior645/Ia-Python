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

# url = "http://webhose.io/filterWebContent?token=b1b86608-f5dc-41e3-89c9-5f9bbbdf0a0f&format=json&ts=1540037188321&sort=crawled&q=bolsonaro%20language%3Aenglish"

# res = requests.get(url)

# materias = res.json()['posts']

# for a in materias:
#     print( a['thread']['url'] )
#     print( a['thread']['site'] )
#     print( a['thread']['title'] )
#     print(a['thread']['site_type'])
#     print(a['thread']['text'])
#     print('---------------------_----------_----')

# stopWords = [
#     'de',
#     'a',
#     'o',
#     'que',
#     'e',
#     'do',
#     'da',
#     'em',
#     'um',
#     'para',
#     'é',
#     'com',
#     'não',
#     'uma',
#     'os',
#     'no',
#     'se',
#     'na',
#     'por',
#     'mais',
#     'as',
#     'dos',
#     'como',
#     'mas',
#     'foi',
#     'ao',
#     'ele',
#     'das',
#     'tem',
#     'à',
#     'seu',
#     'sua',
#     'ou',
#     'ser',
#     'quando',
#     'muito',
#     'há',
#     'nos',
#     'já',
#     'está',
#     'eu',
#     'também',
#     'só',
#     'pelo',
#     'pela',
#     'até',
#     'isso',
#     'ela',
#     'entre',
#     'era',
#     'depois',
#     'sem',
#     'mesmo',
#     'aos',
#     'ter',
#     'seus',
#     'quem',
#     'nas',
#     'me',
#     'esse',
#     'eles',
#     'estão',
#     'você',
#     'tinha',
#     'foram',
#     'essa',
#     'num',
#     'nem',
#     'suas',
#     'meu',
#     'às',
#     'minha',
#     'têm',
#     'numa',
#     'pelos',
#     'elas',
#     'havia',
#     'seja',
#     'qual',
#     'será',
#     'nós',
#     'tenho',
#     'lhe',
#     'deles',
#     'essas',
#     'esses',
#     'pelas',
#     'este',
#     'fosse',
#     'dele',
#     'tu',
#     'te',
#     'vocês',
#     'vos',
#     'lhes',
#     'meus',
#     'minha',
#     'teu',
#     'tu',
#     'teu',
#     'tua',
#     'nosso',
#     'noss',
#     'nosso',
#     'nossa',
#     'dela',
#     'delas',
#     'esta',
#     'estes',
#     'estas',
#     'aquele',
#     'aquela',
#     'aqueles',
#     'aquelas',
#     'isto',
#     'aquilo',
#     'estou',
#     'está',
#     'estamos',
#     'estão',
#     'estive',
#     'esteve',
#     'estivemos',
#     'estiveram',
#     'estava',
#     'estávamos',
#     'estavam',
#     'estivera',
#     'estivéramos',
#     'esteja',
#     'estejamos',
#     'estejam',
#     'estivesse',
#     'estivéssemos',
#     'estivessem',
#     'estiver',
#     'estivermos',
#     'estiverem',
#     'hei',
#     'há',
#     'havemos',
#     'hão',
#     'houve',
#     'houvemos',
#     'houveram',
#     'houvera',
#     'houvéramos',
#     'haja',
#     'hajamos',
#     'hajam',
#     'houvesse',
#     'houvéssemos',
#     'houvessem',
#     'houver',
#     'houvermos',
#     'houverem',
#     'houverei',
#     'houverá',
#     'houveremos',
#     'houverão',
#     'houveria',
#     'houveríamos',
#     'houveriam',
#     'sou',
#     'somos',
#     'são',
#     'era',
#     'éramos',
#     'eram',
#     'fui',
#     'foi',
#     'fomos',
#     'foram',
#     'fora',
#     'fôramos',
#     'seja',
#     'sejamos',
#     'sejam',
#     'fosse',
#     'fôssemos',
#     'fossem',
#     'for',
#     'formos',
#     'forem',
#     'serei',
#     'será',
#     'seremos',
#     'serão',
#     'seria',
#     'seríamos',
#     'seriam',
#     'tenho',
#     'tem',
#     'temos',
#     'tém',
#     'tinha',
#     'tínhamos',
#     'tinham',
#     'tive',
#     'teve',
#     'tivemos',
#     'tiveram',
#     'tivera',
#     'tivéramos',
#     'tenha',
#     'tenhamos',
#     'tenham',
#     'tivesse',
#     'tivéssemos',
#     'tivessem',
#     'tiver',
#     'tivermos',
#     'tiverem',
#     'terei',
#     'terá',
#     'teremos',
#     'terão',
#     'teria',
#     'teríamos',
#     'teriam'
# ]

# import nltk

# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context


# nltk.download()