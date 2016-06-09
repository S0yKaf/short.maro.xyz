angular.module('App',['ngMaterial', 'ngMessages'])
  .controller('IndexController', function ($scope, $http) {
    $scope.test = "this is a test var";
  });
