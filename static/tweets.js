angular.module('tweetsApp', [])
	.controller('TweetListCtrl', ['$scope', '$http', function($scope, $http) {
	    $scope.submit = function() {
	      if ($scope.handle) {
            $http.get('http://127.0.0.1:5000/tweets/' + $scope.handle + "/").success(function(data) {
  					$scope.tweets = data['tweets'];      
  				});
        }
        if ($scope.handle) {
            $http.get('http://127.0.0.1:5000/user/' + $scope.handle + "/").success(function(data) {
  					$scope.user = data['user'];
        	});
        }
  		}
		}]);