var myApp = angular.module('workoutPlanner', ['ui.router', 'oc.lazyLoad', 'ui.bootstrap', ]);

myApp.config(function($stateProvider, $httpProvider) {

  //$urlRouterProvider.otherwise('/');

  //Make sure Django is not complaining about missing CSRF cookie:
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

  $stateProvider

  .state('home', {
    url: '/',
    template: '<workout-planner></workout-planner>',
    cache: false,
    disableCache: true,
    resolve: {
      deps: ['$ocLazyLoad', function($ocLazyLoad) {

        //extra css:
        return $ocLazyLoad.load([
          //'/static/workoutPlanner/components/workoutPlanner/workoutPlanner.css',
        ])
        //extra js:
        .then(function(){
          return $ocLazyLoad.load([
            '/static/components-font-awesome/css/fontawesome-all.css',
          ]);

        })
        .then(function(){
          return $ocLazyLoad.load([
            //Main parent component files:
            '/static/components/workoutPlanner/workoutPlanner.model.js',
            '/static/components/workoutPlanner/workoutPlanner.component.js',

            //Child components:
            '/static/components/workoutPlanner/workouts/workouts.model.js',
            '/static/components/workoutPlanner/workouts/workouts.component.js',
          ]);
        });

      }]
    }

  });

});
