'use strict';

var workoutPlannerController = function($rootScope, $scope, workoutPlannerModel) {

  var ctrl = this;
  ctrl.model = workoutPlannerModel;

  ctrl.$onInit = function() {
  };

};

angular
  .module('workoutPlanner')
  .component('workoutPlanner', {
    templateUrl: '/static/components/workoutPlanner/workout-planner.html',
    controller: workoutPlannerController,
  });
