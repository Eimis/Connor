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

    //A method to edit workout plan instance:
    function submitData(workout_plan, users, workout_exercises) {

      var config = {
        headers: {
          'Accept': 'application/json'
        },
      };

      //m2m users:
      var updated_users = [];
      for (var i = 0; i < users.length; i++) {
        var user_pk = users[i];

        updated_users.push({'pk': user_pk});
      }

      //m2m exercises:
      var updated_exercises = [];
      for (var i = 0; i < workout_exercises.length; i++) {
        var exercise_pk = workout_exercises[i];

        updated_exercises.push({'pk': exercise_pk});
      }

      var data = {
        name: workout_plan.name,
        workout_exercises: updated_exercises,
        users: updated_users,
      };

      return $http.patch('/workout_plans/' + workout_plan.pk + '/update', data, config)
        .then(function(response) {
          return {'ok': true};
        })
        .catch(function(response) {
          return {'errors': response.data};
        });
    }

    //A method to remove workout plan instance:
    function removeData(workout_plan) {

      var config = {
        headers: {
          'Accept': 'application/json'
        },
      };

      return $http.delete('/workout_plans/' + workout_plan.pk + '/remove', config)
        .then(function(response) {
          return {'ok': true};
        })
        .catch(function(response) {
          return {'errors': response.data};
        });
    }

    //A method to remove workout plan instance:
    function createData(workout_plan) {

      var config = {
        headers: {
          'Accept': 'application/json'
        },
      };

      var data = {
        name: workout_plan.name,
        //workout_exercises: updated_exercises,
        //users: updated_users,
      };

      return $http.post('/workout_plans/create', data, config)
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
      removeData: removeData,
      createData: createData,
    };
  });
