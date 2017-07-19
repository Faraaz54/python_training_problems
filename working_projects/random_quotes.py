import requests
import json
import random
quote_type = ('famous','movies')
payload = {'cat': random.choice(quote_type),'count': 2}
response = requests.post("https://andruxnet-random-famous-quotes.p.mashape.com/",params=payload,
  headers={
    "X-Mashape-Key": "37fbdSLhJcmshYEtPo6FTZu5cU4Xp1wBL4WjsnQZ3EVtuJBNty",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  }
)

data = json.loads(response.text)
if payload['count'] == 1:
    if payload['cat'] == 'movies':
        print'Category:- {0}\nQuote:- {1}\nFilm:-{2}'.format(data['category'],data['quote'],data['author'])
    else:
        print'Category:- {0}\nQuote:- {1}\nAuthor:-{2}'.format(data['category'],data['quote'],data['author'])

else:
    for quotes in data:
        print'Category:- {0}\nQuote:- {1}\nAuthor:-{2}\n\n'.format(quotes['category'], quotes['quote'], quotes['author'])




