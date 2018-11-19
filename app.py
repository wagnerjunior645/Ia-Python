# Usado para Trabalhar com json
# Python To Json
# print(json.dumps(twitterApiToken))
# Json to python
# y = json.loads(x)
from twython import Twython
import json

# WRJ2vXrcxjupEOrU3OnWvPSYR (API key)
# JCpVqyxP0HREi7QzOw40XKpo1tBUA1Sqdz7mqbnWC9PHfc96KJ (API secret key)
# 846081728024338432-GssizVAlSpMiZxCOtZfvbpUik6NcflQ (Access token)
# L2pJad7fRaoqkqcGvArbdKV4Nsjwdru7mbkit04MLXexG (Access token secret)
twitterApiToken = {
    'apiKey': 'aj78W3REIbT3fK2j2647Jqq5U',
    'apiSecretKey': 'uY5uViQoEBzhTeovV0aflshsk3wPYtePVxGV8hEJ6fSHU2Fqn2',
    'accessToken': '1064190476172099584-foWii6RfYkCYFDAAKPac7FH2f7TmID',
    'accessTokenSecret': '8IS1DEpTuHLONjCwxQ3XMNQ8noDIxqsWyytjIHNHE5o6O'
}

twitter = Twython(twitterApiToken['apiKey'], twitterApiToken['apiSecretKey'],
                  twitterApiToken['accessToken'], twitterApiToken['accessTokenSecret'])

                  

# twitter.get_home_timeline()

search_results = twitter.search(count=100, q='python')

# Pegar os twitters do usuario especifico, maximo de twitters e de 1 semana
try:
    user_timeline = twitter.get_user_timeline(screen_name='adolfoguimaraes')
except TwythonError as e:
   print (e)
   print('Ocorreu um error ao tentar pegar os twetters da timeline')

print(user_timeline)

count = 1
for tweets in user_timeline:
   print (str(count) + '->' + tweets['text'])
   count += 1
