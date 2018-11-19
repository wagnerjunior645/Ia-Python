from django.http import HttpResponse
from django.shortcuts import render

import requests
import json

def homepage(request, post_id):

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