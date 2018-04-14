'use strict';

var workoutsController = function($rootScope, $scope, $uibModal, workoutsModel) {

  var ctrl = this;
  ctrl.model = workoutsModel;

  ctrl.$onInit = function() {
    syncData();
  };

  var syncData = function() {
    ctrl.model.listData().then(function(resp){
      ctrl.workout_plans = resp.workout_plans;
    });
  }

  var workoutPlanEditModalController = function($scope, $uibModalInstance, workout_plan) {
    var $ctrl = this;

    $ctrl.workout_plan = workout_plan;

    //copy data for resetting it if modal was closed:
    var original_workout_plan = angular.copy($ctrl.workout_plan);

    //Initial users:
    var selected_users = [];
    for (var key in workout_plan.users) {
      var e = workout_plan.all_users[key];
      selected_users.push(e.pk);
    }
    $ctrl.selected_users = selected_users;

    //Initial exercises:
    var selected_exercises = [];
    for (var key in workout_plan.workout_exercises) {
      var e = workout_plan.workout_exercises[key];
      selected_exercises.push(e.pk);
    }
    $ctrl.selected_exercises = selected_exercises;

    $ctrl.updateWorkoutPlan = function(workout_plan, users, workout_exercises) {
      //console.log(workout_plan, workout_exercises)
      ctrl.model.submitData(workout_plan, users, workout_exercises).then(function(resp){
        if (resp.ok) {
          $uibModalInstance.dismiss('cancel');
          syncData();
        }
      });
    };

    $ctrl.cancel = function() {
      //reset value if editing was canceled:
      angular.copy(original_workout_plan, $ctrl.workout_plan);
      $uibModalInstance.dismiss('cancel');
    };
  };

  ctrl.openWorkoutPlanEditModal = function(workout_plan) {
    var parentElem = angular.element(document).find('body');

    var uploadModalInstance = $uibModal.open({
      animation: true,
      keyboard: false,
      ariaLabelledBy: 'modal-title',
      ariaDescribedBy: 'modal-body',
      templateUrl: 'workoutPlanEditModalContent.html',
      controller: workoutPlanEditModalController,
      scope: $scope, //passed current scope to the modal
      controllerAs: '$ctrl',
      appendTo: parentElem,
      //extra info for modal:
      resolve: {
        workout_plan: function() {
          return workout_plan;
        },
      }
    });

    uploadModalInstance.result.then(function() {
      //console.log('clicked OK')
    }, function() {
      //console.log('clicked CANCEL')
    });
  };

};

angular
  .module('workoutPlanner')
  .component('workouts', {
    templateUrl: '/static/components/workoutPlanner/workouts/workouts.html',
    controller: workoutsController,
  });
