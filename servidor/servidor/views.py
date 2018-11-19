from django.http import HttpResponse
from django.shortcuts import render

import requests
import json

def homepage(request, post_id):

    queryUrl = 'https://newsapi.org/v2/everything?' + 'q=' + str(post_id) + '&' + 'language=pt&' + 'sortBy=popularity&' + 'apiKey=a59b3dfb9d3f410f86db9bf2b505be0a'

    url = (queryUrl)

    res = requests.get(url)

    artigos = res.json()['articles']
    countArtigos = len(artigos)

    return render(request, 'index.html', {'artigos': artigos, 'countArtigos': countArtigos})