'use strict';

var workoutsController = function($rootScope, $scope, $uibModal, workoutsModel) {

  var ctrl = this;
  ctrl.model = workoutsModel;

  ctrl.$onInit = function() {
    ctrl.model.getExtraData().then(function(resp){
      $scope.all_exercises = resp.all_exercises;
      $scope.all_users = resp.all_users;
    });

    syncData();
  };

  var syncData = function() {
    ctrl.model.listData().then(function(resp){
      ctrl.workout_plans = resp.workout_plans;
    });
  };

  ////////////////////////////
  // EDITING WORKOUT PLANS ///
  ////////////////////////////
  //
  var workoutPlanEditModalController = function($scope, $uibModalInstance, workout_plan) {
    var $ctrl = this;

    $ctrl.workout_plan = workout_plan;

    //This comes from 'extra_data/' api endpoint:
    $ctrl.all_users = $scope.all_users;
    $ctrl.all_exercises = $scope.all_exercises;

    //copy data for resetting it if modal was closed:
    var original_workout_plan = angular.copy($ctrl.workout_plan);

    //Initial users:
    var selected_users = [];
    for (var key in workout_plan.users) {
      var e = $scope.all_users[key];
      selected_users.push(e.pk);
    }
    $ctrl.selected_users = selected_users;

    //Initial exercises:
    var selected_exercises = [];
    for (var key in workout_plan.workout_exercises) {
      var e = $scope.all_exercises[key];
      selected_exercises.push(e.pk);
    }
    $ctrl.selected_exercises = selected_exercises;

    $ctrl.updateWorkoutPlan = function(workout_plan, users, workout_exercises) {
      $ctrl.errors = [];

      ctrl.model.submitData(workout_plan, users, workout_exercises).then(function(resp){
        if (resp.errors) {
          $ctrl.errors = resp.errors[$ctrl.workout_plan.pk];
        }
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

  ctrl.removeWorkoutPlan = function(workout_plan) {
    ctrl.model.removeData(workout_plan).then(function(resp){
      syncData();
    });
  };

  ////////////////////////////
  // CREATING WORKOUT PLANS //
  ////////////////////////////
  //
  var workoutPlanCreateModalController = function($scope, $uibModalInstance) {
    var $ctrl = this;

    //This comes from 'extra_data/' api endpoint:
    $ctrl.all_users = $scope.all_users;
    $ctrl.all_exercises = $scope.all_exercises;

    $ctrl.workout_plan = {};

    $ctrl.createWorkoutPlan = function() {
      $ctrl.errors = [];

      ctrl.model.createData($ctrl.workout_plan).then(function(resp){
        if (resp.errors) {
          $ctrl.errors = resp.errors;
        }
        if (resp.ok) {
          $uibModalInstance.dismiss('cancel');
          syncData();
        }
      });
    };

    $ctrl.cancel = function() {
      $uibModalInstance.dismiss('cancel');
    };
  };

  ctrl.openWorkoutPlanCreateModal = function() {
    var parentElem = angular.element(document).find('body');

    var editModalInstance = $uibModal.open({
      animation: true,
      keyboard: false,
      ariaLabelledBy: 'modal-title',
      ariaDescribedBy: 'modal-body',
      templateUrl: 'workoutPlanCreateModalContent.html',
      controller: workoutPlanCreateModalController,
      scope: $scope, //passed current scope to the modal
      controllerAs: '$ctrl',
      appendTo: parentElem,
    });

    editModalInstance.result.then(function() {
      //console.log('clicked OK')
    }, function() {
      //console.log('clicked CANCEL')
    });
  };

  ///////////////////////////
  // VIEWING EXERCISE INFO //
  ///////////////////////////
  //
  var workoutExerciseInfoModalController = function($scope, $uibModalInstance, workout_exercise) {
    var $ctrl = this;

    $ctrl.workout_exercise = workout_exercise;

    $ctrl.cancel = function() {
      $uibModalInstance.dismiss('cancel');
    };
  };

  ctrl.openWorkoutExerciseInfoModal = function(workout_exercise) {
    var parentElem = angular.element(document).find('body');

    var uploadModalInstance = $uibModal.open({
      animation: true,
      keyboard: false,
      ariaLabelledBy: 'modal-title',
      ariaDescribedBy: 'modal-body',
      templateUrl: 'workoutExerciseInfoModalContent.html',
      controller: workoutExerciseInfoModalController,
      scope: $scope, //passed current scope to the modal
      controllerAs: '$ctrl',
      appendTo: parentElem,
      //extra info for modal:
      resolve: {
        workout_exercise: function() {
          return workout_exercise;
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
