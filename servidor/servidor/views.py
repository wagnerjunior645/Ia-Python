from django.http import HttpResponse
from django.shortcuts import render
from string import punctuation

import requests
import json

from twython import Twython

stopWords = [
    'de',
    'a',
    'o',
    'que',
    'e',
    'do',
    'da',
    'em',
    'um',
    'para',
    'é',
    'com',
    'não',
    'uma',
    'os',
    'no',
    'se',
    'na',
    'por',
    'mais',
    'as',
    'dos',
    'como',
    'mas',
    'foi',
    'ao',
    'ele',
    'das',
    'tem',
    'à',
    'seu',
    'sua',
    'ou',
    'ser',
    'quando',
    'muito',
    'há',
    'nos',
    'já',
    'está',
    'eu',
    'também',
    'só',
    'pelo',
    'pela',
    'até',
    'isso',
    'ela',
    'entre',
    'era',
    'depois',
    'sem',
    'mesmo',
    'aos',
    'ter',
    'seus',
    'quem',
    'nas',
    'me',
    'esse',
    'eles',
    'estão',
    'você',
    'tinha',
    'foram',
    'essa',
    'num',
    'nem',
    'suas',
    'meu',
    'às',
    'minha',
    'têm',
    'numa',
    'pelos',
    'elas',
    'havia',
    'seja',
    'qual',
    'será',
    'nós',
    'tenho',
    'lhe',
    'deles',
    'essas',
    'esses',
    'pelas',
    'este',
    'fosse',
    'dele',
    'tu',
    'te',
    'vocês',
    'vos',
    'lhes',
    'meus',
    'minha',
    'teu',
    'tu',
    'teu',
    'tua',
    'nosso',
    'noss',
    'nosso',
    'nossa',
    'dela',
    'delas',
    'esta',
    'estes',
    'estas',
    'aquele',
    'aquela',
    'aqueles',
    'aquelas',
    'isto',
    'aquilo',
    'estou',
    'está',
    'estamos',
    'estão',
    'estive',
    'esteve',
    'estivemos',
    'estiveram',
    'estava',
    'estávamos',
    'estavam',
    'estivera',
    'estivéramos',
    'esteja',
    'estejamos',
    'estejam',
    'estivesse',
    'estivéssemos',
    'estivessem',
    'estiver',
    'estivermos',
    'estiverem',
    'hei',
    'há',
    'havemos',
    'hão',
    'houve',
    'houvemos',
    'houveram',
    'houvera',
    'houvéramos',
    'haja',
    'hajamos',
    'hajam',
    'houvesse',
    'houvéssemos',
    'houvessem',
    'houver',
    'houvermos',
    'houverem',
    'houverei',
    'houverá',
    'houveremos',
    'houverão',
    'houveria',
    'houveríamos',
    'houveriam',
    'sou',
    'somos',
    'são',
    'era',
    'éramos',
    'eram',
    'fui',
    'foi',
    'fomos',
    'foram',
    'fora',
    'fôramos',
    'seja',
    'sejamos',
    'sejam',
    'fosse',
    'fôssemos',
    'fossem',
    'for',
    'formos',
    'forem',
    'serei',
    'será',
    'seremos',
    'serão',
    'seria',
    'seríamos',
    'seriam',
    'tenho',
    'tem',
    'temos',
    'tém',
    'tinha',
    'tínhamos',
    'tinham',
    'tive',
    'teve',
    'tivemos',
    'tiveram',
    'tivera',
    'tivéramos',
    'tenha',
    'tenhamos',
    'tenham',
    'tivesse',
    'tivéssemos',
    'tivessem',
    'tiver',
    'tivermos',
    'tiverem',
    'terei',
    'terá',
    'teremos',
    'terão',
    'teria',
    'teríamos',
    'teriam'
]

def homepage(request, post_id):

    twitterApiToken = {
    'apiKey': 'aj78W3REIbT3fK2j2647Jqq5U',
    'apiSecretKey': 'uY5uViQoEBzhTeovV0aflshsk3wPYtePVxGV8hEJ6fSHU2Fqn2',
    'accessToken': '1064190476172099584-foWii6RfYkCYFDAAKPac7FH2f7TmID',
    'accessTokenSecret': '8IS1DEpTuHLONjCwxQ3XMNQ8noDIxqsWyytjIHNHE5o6O'
    }

    twitter = Twython(twitterApiToken['apiKey'], twitterApiToken['apiSecretKey'],
        twitterApiToken['accessToken'], twitterApiToken['accessTokenSecret'])

    try:
        user_timeline = twitter.get_user_timeline(screen_name=post_id)
    except TwythonError as e:
        print (e)
        print('Ocorreu um error ao tentar pegar os twetters da timeline')

    # print(user_timeline)
    arrayFinal = []
    for tweets in user_timeline:
        print(tweets['text'])
        palavra = removerCaracteresEspeciais(tweets['text'])
        print(palavra)
        arrayPalavra = palavra.split(' ')

        for bbc in arrayPalavra:
            if bbc not in stopWords:
                arrayFinal.append(bbc)

    print(arrayFinal)

    # frase1 = 'wagner, júnior meu ovo legal para você'

    # fraseArray = frase1.split(' ')

    queryUrl_site2 = "http://webhose.io/filterWebContent?token=b1b86608-f5dc-41e3-89c9-5f9bbbdf0a0f&format=json&ts=1540037188321&sort=crawled&" + "q=" + str(post_id) + "%20language%3Aenglish"
    queryUrl = 'https://newsapi.org/v2/everything?' + 'q=' + str(post_id) + '&' + 'language=pt&' + 'sortBy=popularity&' + 'apiKey=a59b3dfb9d3f410f86db9bf2b505be0a'

    url1 = (queryUrl)
    url2 = (queryUrl_site2)

    res = requests.get(url1)
    res2 = requests.get(url2)

    artigos = res.json()['articles']

    artigos2 = res2.json()['posts']

    for a in artigos2:
        j = {
            'urlToImage': '',
            'title': a['thread']['title'],
            'description': a['thread']['title_full'],
            'url': a['thread']['url']
        }
        artigos.append(j)

    countArtigos = len(artigos)
    return render(request, 'index.html', {'artigos': artigos, 'countArtigos': countArtigos})


# Retirar acentuacao
from unicodedata import normalize	
def removerCaracteresEspeciais (text) :
	return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')