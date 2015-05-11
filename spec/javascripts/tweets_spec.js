
describe('TweetListCtrl', function() {
   var $httpBackend, $rootScope, createController, authRequestHandler;

   // Set up the module
   beforeEach(module('tweetsApp'));

   beforeEach(inject(function(_$httpBackend_, $rootScope, $controller) {
     $httpBackend = _$httpBackend_;
     
     scope = $rootScope.$new();
     scope.handle = "ydawant";
     ctrl = $controller('TweetListCtrl', {$scope: scope});
   })
   );
   afterEach(function() {
     $httpBackend.verifyNoOutstandingExpectation();
     $httpBackend.verifyNoOutstandingRequest();
   });

  it("should do anything", function(){
    expect(true).toBe(true);
  });
});

