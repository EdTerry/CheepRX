angular.module('CheepRX', ['ngCookies'])
    .controller('HomeCtrl', function($scope, $http, $timeout, $window, $cookies) {

    $scope.info = {};
    $scope.storename = "";

        // SHOW DEALS LIST
    $scope.getCouponList = function(){
      $http({
        method: 'POST',
        url: '/getCouponList',

      }).then(function(response) {
        $scope.storename = response.data;
        console.log('mm',$scope.storename);

          console.log("Load complete");
      }, function(error) {
        console.log(error);
      });
    }

    // SUBMIT COUPON - DODO
    $scope.submitRX = function(){
      $http({
        method: 'POST',
        url: '/submitRX',
        data: {info:$scope.info}
      }).then(function(response) {

        $scope.getCouponList();
        $scope.info = {}
        console.log("Added.");
      }, function(error) {
        console.log(error);
      });
    }

        $scope.getCouponList();
    })
