angular.module('workoutPlanner')
  .factory('workoutsModel', function($http) {

    //A method to list all current Workout plans:
    function listData() {

      var config = {
        headers: {
          'Accept': 'application/json'
        },
      };

      return $http.get('/workout_plans/list', config)
        .then(function(response) {
          var workout_plans = angular.fromJson(response.data);

          return {
            workout_plans: workout_plans,
          };
        })
        .catch(function(response) {});
    }

    return {
      listData: listData,
      //submitData: submitData,
      //getStats: getStats,
    };
  });
