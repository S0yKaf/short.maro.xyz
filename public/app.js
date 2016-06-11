angular.module('App',[])
  .controller('IndexController', function ($scope, $http) {
    $scope.shorten = function () {
      var data = {
           url: $scope.url,
       }

       $http.post('/', data)
           .success(function(data) {
               $scope.url = data.short_url;
           })
           .error(function(err, status) {
               $scope.error = {message: err.error, status: status};
           });
   };
  });
