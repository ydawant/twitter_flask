
class Tweet(object):
  def __init__(self, id, text, retweet_count, created_at, picture=None, influence_score=0):
    self.id = id
    self.retweet_count = retweet_count
    self.created_at = created_at
    self.picture = picture
    self.text = text
    self.influence_score = influence_score

  def serialize(self):
    return {
      "id": self.id,
      "text": self.text,
      "retweet_count": self.retweet_count,
      "created_at": self.created_at,
      "picture": self.picture,
      "influence_score": self.influence_score
    }

class User(object):
  def __init__(self, id, description, followers, following):
    self.id = id
    self.description = description
    self.followers = followers
    self.following = following

  def serialize(self):
    return {
      "id" : self.id,
      "description": self.description,
      "followers": self.followers,
      "following": self.following
    }