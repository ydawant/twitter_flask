angular.module('tweetsApp', [])
	.controller('TweetListCtrl', ['$scope', '$http', '$filter', function($scope, $http, $filter) {
	    $scope.submit = function() {
	      if ($scope.handle) {
            $http.get('https://twitter-flask.herokuapp.com/tweets/' + $scope.handle + "/").success(function(data) {
            $scope.tweets = data['tweets'];
  				});
        }
        if ($scope.handle) {
            $http.get('https://twitter-flask.herokuapp.com/user/' + $scope.handle + "/").success(function(data) {
  					$scope.user = data['user'];
        	});
        }

        $scope.picFilter = function(tweets) {
          if ($scope.search == 'picture') {
            return $filter('filter')($scope.tweets, {picture:'!null'});
          }
          else {
            return $scope.tweets
          }
        }

        $scope.getProfileScore = function() {
          var score = 0;
          if ($scope.tweets && $scope.user) {
            for(i=0; i < $scope.tweets.length; i++) {
              score += $scope.tweets[i].influence_score
            } 
            score += $scope.user.followers
            return score
          }
        }
      }
    }]
  );
