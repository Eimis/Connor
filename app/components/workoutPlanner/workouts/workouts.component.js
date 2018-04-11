'use strict';

var workoutsController = function($rootScope, $scope, workoutsModel) {

  var ctrl = this;
  ctrl.model = workoutsModel;

  ctrl.$onInit = function() {
    console.log('inited');
  };

};

angular
  .module('workoutPlanner')
  .component('workouts', {
    templateUrl: '/static/components/workoutPlanner/workouts/workouts.html',
    controller: workoutsController,
  });
