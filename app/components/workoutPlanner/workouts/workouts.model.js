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

    function submitData(workout_plan, workout_exercises) {

      var config = {
        headers: {
          'Accept': 'application/json'
        },
      };

      var updated_exercises = [];
      for (var i = 0; i < workout_exercises.length; i++) {
        var exercise_pk = workout_exercises[i];

        updated_exercises.push({'pk': exercise_pk});
      }

      var data = {
        name: workout_plan.name,
        workout_exercises: updated_exercises,
      };

      return $http.patch('/workout_plans/' + workout_plan.pk + '/update', data, config)
        .then(function(response) {
          return {'ok': true};
        })
        .catch(function(response) {
          return {'errors': response.data};
        });
    }

    return {
      listData: listData,
      submitData: submitData,
      //getStats: getStats,
    };
  });
