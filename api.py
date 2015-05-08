from flask import Flask, render_template, jsonify
from helper_methods import influence_score_calc
from models import Tweet
from twitter_client import get_twitter_api

app = Flask(__name__)

# api = get_twitter_api()

api = get_twitter_api()


#need to render the initial page... all the rest is JSON.
@app.route("/", methods=['GET'])
def index():
  return render_template("index.html")

@app.route("/user/<handle>/", methods=['GET'])
def user(handle):
  pass

@app.route("/tweets/<handle>/", methods=['GET'])
def tweets(handle):
  statuses = api.GetUserTimeline(handle)

  tweet_list = []
  for s in statuses:
    tweet = Tweet(id = s.id, text=s.text, retweet_count = s.retweet_count,
      created_at = s.created_at, influence_score=influence_score_calc(s.text),
      picture = (None if s.media==[] else s.media[0].get("media_url", None)))
    tweet_list.append(tweet)

  return jsonify(tweets=[tweet.serialize() for tweet in tweet_list])

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
  app.run(debug=True)
