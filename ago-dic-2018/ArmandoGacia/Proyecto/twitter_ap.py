from Tweet import Tweeti
from Tweet  import Abstracttweet
import tweepy
from tweepy import OAuthHandler

class AppTwitter(Abstracttweet):
    def getUsuario(self, handle):
        #Datos para Autentificación
        consumer_key = 'j7bXwQAiFE0EIcCrptRIbANGP'
        consumer_secret = 'WX41oCT4SOK12vZEQYPqM1KHw2sukIknTjWaleX8BvVahi7ull'
        access_token = '832311984-34Nv5J7AViBapsD22x8KZQE5mMPzcSaA2pzVbDyt'
        access_token_secret = 'zeIKKumVBMwOxEBDhJg8Qh7bDtu6bjne7QWi1qsFgfJ9A'
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)

        #Autentificación
        api = tweepy.API(auth)
        try:
            user = api.get_user(screen_name=handle)
            user_id = user.id_str
            lugar = user.location

            if (user.verified == True):
                verificado = 'Si.'
            else:
                verificado = 'Usuario no verificado.'

            followers = user.followers_count
            numtweets= user.statuses_count
            friends = user.friends_count

            if (user.description == ''):
                description = 'No tiene.'
            else:
                description = user.description

            lenguaje = user.lang
            profile = user.profile_image_url
            Ranking= None
            Categoria= None
            Victorias= 0
            Derrotas= 0
        except tweepy.error.TweepError:
                print ('-- ' + handle + ' not found')
        print ('Fetching %' + handle)
        return Tweeti(user_id,handle,lugar,verificado,followers,numtweets,friends,description,lenguaje,profile,Ranking,Categoria,Victorias,Derrotas)
if __name__ == '__main__':
    y=AppTwitter()
    twwt = y.getUsuario('DavidDarkXD')
    print(twwt.description)
