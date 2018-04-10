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
* create a virtual environment `virtualenv virtualenv`
* run `source virtual/bin/activate` to activate your fresh virtual environment
* run `pip install -r requirements.txt` to install backend dependencies
* run `cd connor/ && ./manage.py migrate` to run migrations (sqlite db is used)
* run `./manage.py collectstatic`
* `./manage.py runserver`
* Visit http://localhost:8000
