angular.module('workoutPlanner')
  .factory('workoutPlannerModel', function($http) {

    //Synchronizes data with backend server:
    function updateData(scope, items) {

      //var config = {
        //headers: {
          //'Accept': 'application/json'
        //},
      //};

      //var data = {
        //items: items,
      //};

      //return $http.post('/issues/update', data, config)
        //.then(function(response) {
          //return true;
        //})
        //.catch(function(response) {});
    }

    return {
      updateData: updateData,
    };
  });
