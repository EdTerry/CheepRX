angular.module('CheepRX', ['ngCookies'])
    .controller('HomeCtrl', function($scope, $http, $timeout, $window, $cookies) {

$scope.info = {};

$scope.showAdd = true;
        $scope.loadComplete = false;
        $scope.refreshing = false;

        $scope.lastRefresh = "";

        //Sorting
        $scope.orderByField = 'device';
        $scope.reverseSort = false;

        $scope.tickerName = "";

        // SHOW DEALS LIST
    $scope.showlist = function(){
                $scope.loadComplete = false;
      $http({
        method: 'POST',
        url: '/getTickerList',

      }).then(function(response) {
        $scope.tickers = response.data;
        console.log('mm',$scope.tickers);

                    console.log("Load complete");

                    $scope.loadComplete = true;
      }, function(error) {
                    $scope.loadComplete = true;
        console.log(error);
      });
    }

    $scope.refreshTickers = function(){
                $scope.loadComplete = false;
      $http({
        method: 'POST',
        url: '/refreshTickers',

      }).then(function(response) {
                    console.log("Refresh complete");
                    $scope.loadComplete = true;

                    $scope.showlist();
                    $scope.info = {}
      }, function(error) {
                    $scope.loadComplete = true;
        console.log(error);
      });
    }

    // SUBMIT COUPON - DODO
    $scope.addTicker = function(){
      $http({
        method: 'POST',
        url: '/addTicker',
        data: {info:$scope.info}
      }).then(function(response) {
        $scope.showlist();
        $('#addPopUp').modal('hide')
        $scope.info = {}
                    console.log("Added.");
      }, function(error) {
        console.log(error);
      });
    }

    // OPEN COUPON WINDOW
    $scope.showStockTwits = function(tickerName){
          window.open("https://stocktwits.com/symbol/"+tickerName+"?popout=true&substream=top", "newwindow", "width=800,height=600");
    }

    // SHOW COUPON CHART
    $scope.showTickerChart = function(tickerName){
      $scope.showChart = true;
                $scope.tickerName = tickerName;
      $scope.info = {};
                console.log($scope.tickerName);
      $('#displayChart').modal('show')
    }

        $scope.showlist();
    })
