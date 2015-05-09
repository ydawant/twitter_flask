import twitter

def get_twitter_api():
  api = twitter.Api(consumer_key='rgOxicfxYYy9DbaHBdYTdH7yb',
                      consumer_secret='aGBYoGEp13HnGWAtnauXoTVJXGAFoShdNgBTee5UpbSEGumCj6',
                      access_token_key='1212470810-QfU4KZB90PcNk2uT9IJGBvNAdb9b4z8vKkvHmLT',
                      access_token_secret='nQFDHyjt8yhFevW0hAlWdQDdIPHuSShJMFsrgMTiVx51M')

  return api 
