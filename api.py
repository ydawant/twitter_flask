from flask import Flask, render_template, jsonify, url_for
from helper_methods import influence_score_calc, convert_datetime
from models import Tweet, User
from twitter_client import get_twitter_api
from flask.ext.triangle import Triangle

app = Flask(__name__)
Triangle(app)

# api = get_twitter_api()

api = get_twitter_api()


#need to render the initial page... all the rest is JSON.
@app.route("/", methods=['GET'])
def index():
  return render_template("index.html", script=url_for('static', filename='tweets.js'))

@app.route("/user/<handle>/", methods=['GET'])
def user(handle):
  twitter_user = api.GetUser(screen_name=handle)
  user = User(id = twitter_user.id, name=twitter_user.name, description=twitter_user.description, 
    followers=twitter_user.followers_count, following=twitter_user.friends_count)
  return jsonify(user=user.serialize())

@app.route("/tweets/<handle>/", methods=['GET'])
def tweets(handle):
  statuses = api.GetUserTimeline(screen_name=handle)

  tweet_list = []
  for s in statuses:
    tweet = Tweet(id = s.id, text=s.text, retweet_count = s.retweet_count,
      created_at = convert_datetime(s.created_at), influence_score=influence_score_calc(s.text),
      picture = (None if s.media==[] else s.media[0].get("media_url", None)))
    tweet_list.append(tweet)

  return jsonify(tweets=[tweet.serialize() for tweet in tweet_list])

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
  app.run(debug=True)
