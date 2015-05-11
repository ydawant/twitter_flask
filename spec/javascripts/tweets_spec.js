
describe('TweetListCtrl', function() {
  beforeEach(module('tweetsApp'));

  var tweet = {"created_at": "Sat, 09 May 2015 02:28:59 GMT", "id": 1, 
                  "influence_score": 1, "picture": null, "retweet_count": 4, "text": "good"};

  var pic_tweet = {"created_at": "Sat, 09 May 2015 02:28:59 GMT", "id": 1, 
                  "influence_score": 1, "picture": "picture", "retweet_count": 4, "text": "good"};

  var user = {"id" : 2, "name": "yannick", "description":"testing", "followers":10};
     

  beforeEach(inject(function($injector) {

     $rootScope = $injector.get('$rootScope');
     $rootScope.handle = "ydawant"

     $httpBackend = $injector.get('$httpBackend');
     $httpBackend.when('GET', 'https://twitter-flask.herokuapp.com/tweets/' + $rootScope.handle + "/")
                            .respond({"tweets": [tweet, pic_tweet]});
     $httpBackend.when('GET', 'https://twitter-flask.herokuapp.com/user/' + $rootScope.handle + "/")
                            .respond({"user": user});

     $http = $injector.get('$http');
     $filter = $injector.get('$filter');

     
     var $controller = $injector.get('$controller');

     createController = function() {
       return $controller('TweetListCtrl', {$scope : $rootScope , $http: $http, $filter:$filter});
     };
   }));

  it("should return tweets from the API on submit", function(){
    createController();
    $rootScope.submit();
    $httpBackend.flush();

    var tweets = $rootScope.tweets;
    expect(tweets.length).toBe(2);
    expect(tweets[0].id).toBe(1);
    expect(tweets[0].retweet_count).toBe(4);
  });

  it("should return a user from the API on submit", function (){
    createController();
    $rootScope.submit();
    $httpBackend.flush();
    var user = $rootScope.user;
    expect(user.id).toBe(2);
    expect(user.name).toBe("yannick");
  })

  it("should return correct profile score", function() {
    createController();
    $rootScope.submit();
    $httpBackend.flush();
    var score = $rootScope.getProfileScore();
    expect(score).toBe(12);
  })

  it("should filter out picture tweets", function() {
    createController();
    $rootScope.submit();
    $httpBackend.flush();
    var pics = $rootScope.picFilter()
    expect(pics.length).toBe(2);
    $rootScope.search = "picture"
    var pics = $rootScope.picFilter()
    expect(pics.length).toBe(1);
    

  })
});

