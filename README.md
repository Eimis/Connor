# Connor

![Preview](https://i.imgur.com/UGj1IT4.png "Preview")

A smple app to:

* Create
* Load
* Edit
* Delete

workout plans (plan in ahead).

The app was developed with:

* Python `3.5.2`
* Django `2.0.4`

Setup:

* Clone this repo
* create a virtual environment `python3 -m venv virtualenv`
* run `source virtual/bin/activate` to activate your fresh virtual environment
* run `pip install -r requirements.txt` to install backend dependencies
* run `bower install` to install frontend dependencies
* run `cd connor/ && ./manage.py migrate` to run migrations (sqlite db is used)
* `./manage.py runserver`
* Visit http://localhost:8000/#/ (don't forget the # character!)

Key points:

* When migrations are ran:

   * 7 Initial Week days are created
   * 3 initial `Users` are created:

      * John Doe (login credentials: `john_doe / test`)
      * Linda Doe (`linda_doe / test`)
      * Matthew Doe (`matthew_doe / test`)
   * 1 initial `superuser` account is created, login credentials: `superuser / superuser`:
   * 5 Initial Workout plans are created
   * 4 of the plans are assigned to initial `Users`
   * 20 Initial Workout excercises are created
   * Week days are assigned **randomly** to Workout exercises
   * Workout exercises are assigned **randomly** to Workout plans
   * Workout plans are assigned to the initial `Users`

* The backend is implemented as a RESTful API with `django-rest-framework`,
 serializers, validation, proper error messages and etc.
* Most of the functionality has docstrings and comments, so the code should
 be self-explanatory
* The frontend runs as a separate Angular JS (`1.5.0`) single-page-application
 with a component-based architecture, every component has a `*.component.js`,
 `*.model.js` and `*.html` files. See `app/` directory.
* Currently There's a `<workout-planner></workout-planner>` wrapper component
 and inside of it there's a main `<workouts></workouts>` component which holds
 the core frontend functionality. One can easily move components within
 the app and everything should nicely work autimatically

* Workflow:

   * After visiting `http://localhost:8000/#/` you can **list**, **create**,
     **edit** and **remove**  initial Workout Plans that were created during
     initial migrations, assign different users or exercises to them, change
     name, etc
   * You can also check the api endpoints via `curl`, f. ex.: `curl -d '{"users":[], "workout_exercises":[], "name": "test_name"}' -H "Content-Type: application/json" -X POST http://localhost:8000/workout_plans/create`, but originally one should use
   default fancy inerface for that (`http://localhost:8000/#/`)
   * Django rest framework's default browsable HTML API is disabled because nested
   serializer fields are not supported by it anyway
   * At this point, you can only edit `Users` and `WorkoutExcercise`s via Django
   admin (`http://localhost:8000/admin/`, `superuser` / `superuser`). Although,
   the main app interface displays `WorkoutExercise` info (name, description, assigned week
   days)
   * At this point no API endpoint requires authentication

* Side notes / TODOs:

   * The app is responsive and should work nicely on iPhones as well. Although,
     for the scope of this task, the css is quite messy (because it's a free template
     which was just modified)
   * TODO: ability to edit exercise info via app's interface (not Django admin)
   * Some basic tests
