import json
import unittest
from mock import patch
import twitter
from api import app
from helper_methods import influence_score_calc


class TwitterUser(object):
  def __init__(self, id, name, description, followers_count, friends_count):
    self.id = id
    self.name= name
    self.description = description
    self.followers_count = followers_count
    self.friends_count = friends_count

class Status(object):
  def __init__(self, id, text, retweet_count, created_at, media):
    self.id = id
    self.text = text
    self.retweet_count = retweet_count
    self.created_at = created_at
    self.media = media


class TestApi(unittest.TestCase):

  def setUp(self):
    self.user =  TwitterUser(id=12345,
                             name="yannick",
                             description="fun times",
                             followers_count=10,
                             friends_count=20)

    self.status_1 = Status(id=1,
                           text = "good text",
                           retweet_count=5,
                           created_at="December 2, 2014",
                           media=[{"media_url": "https://www.google.com"}])


    self.status_2 = Status(id=2,
                           text = "bad text",
                           retweet_count=5,
                           created_at="December 2, 2014",
                           media=[])


  def test_index(self):
    response = app.test_client().get('/')
    self.assertEqual(response.status_code, 200)

  @patch.object(twitter.Api, 'GetUser')
  def test_get_user(self, twitter_api):
    twitter_api.return_value = self.user
    response = app.test_client().get('/user/ydawant/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(json.loads(response.data), {u'user': {u'following': 20, u'followers': 10, u'description': u'fun times', u'name': u'yannick', u'id': 12345}})

  @patch.object(twitter.Api, 'GetUserTimeline')
  def test_get_tweets(self, twitter_api):
    twitter_api.return_value = [self.status_1, self.status_2]
    response = app.test_client().get('/tweets/ydawant/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(json.loads(response.data), {u'tweets': [{u'picture': u'https://www.google.com', u'influence_score': 1, u'created_at': u'December 2, 2014', u'text': u'good text', u'retweet_count': 5, u'id': 1},
                                                             {u'picture': None, u'influence_score': -1, u'created_at': u'December 2, 2014', u'text': u'bad text', u'retweet_count': 5, u'id': 2}]})


  def test_influence_score_helper(self):
    good_score = influence_score_calc("text with good thing!")
    bad_score = influence_score_calc("text with bad thing!")
    self.assertEqual(good_score, 1)
    self.assertEqual(bad_score, -1)

if __name__ == '__main__':
  unittest.main()
