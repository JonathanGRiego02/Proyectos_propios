import tweepy
from datetime import datetime

# Coloca tus propias credenciales de la API de Twitter aquí
#API
consumer_key = 'n32nQPuP9BDwsK18Eu1nEZOR1'
consumer_secret = 'VDCg9GWrO7kqSA4I4193VQ5H8UO2oMzLc7jQqiFSHzhzk8T1ql'
access_token = '2412312549-kTbUxMSw1SbC6UEDUB5nztjPJNDzQ5DIlNDq424'
access_token_secret = 'tzBc7LHpqQkoARqn1UzGnii9hVmsX55AER7H6YsqksJwP'

# Configura las credenciales
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Crea un objeto API
api = tweepy.API(auth)

# Nombre de usuario de la cuenta de la que quieres obtener los retweets
nombre_de_usuario = '@cpcxlxrx'

# Número de tweets a recuperar (máximo 200 por solicitud)
num_tweets = 200
ano_especifico = 2019
# Obtén los tweets del usuario
tweets = api.user_timeline(screen_name=nombre_de_usuario, count=num_tweets, tweet_mode="extended")

# Filtra los tweets por año
tweets_ano_especifico = [tweet for tweet in tweets if tweet.created_at.year == ano_especifico]

# Imprime la información de los retweets
for tweet in tweets_ano_especifico:
    print(f'Tweet: {tweet.full_text}')
    print('Retweets:')
    retweets = api.retweets(tweet.id)
    for retweet in retweets:
        print(f'- {retweet.user.screen_name}')
    print('\n')