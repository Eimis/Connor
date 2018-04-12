# Connor

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
* Visit http://localhost:8000

Key points:

* When migrations are ran:

   * Initial Week days are created
   * 3 initial `User`s are created:

      * John Doe (login credentials: `john_doe / test`)
      * Linda Doe (`linda_doe / test`)
      * Matthew Doe (`matthew_doe / test`)

* Important notes:

   * The app is responsive and should work nicely on iPhones as well. Although,
     for the scope of this task, the css is quite messy (because it's a free template
     which was just modified)
