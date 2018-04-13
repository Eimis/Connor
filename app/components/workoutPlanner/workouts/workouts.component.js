'use strict';

var workoutsController = function($rootScope, $scope, workoutsModel) {

  var ctrl = this;
  ctrl.model = workoutsModel;

  ctrl.$onInit = function() {
    ctrl.model.listData().then(function(resp){
      ctrl.workout_plans = resp.workout_plans;
      console.log(ctrl.workout_plans);
    });
  };

};

angular
  .module('workoutPlanner')
  .component('workouts', {
    templateUrl: '/static/components/workoutPlanner/workouts/workouts.html',
    controller: workoutsController,
  });
