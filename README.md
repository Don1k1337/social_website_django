# social_website_django
Pet-project, social website builded with the help of Python, and Django Web framework
This project was implemented with the most required tech stack. Was created a authentication using social Auth (Google/Facebook APIs), activity stream, follow/like system.
Implemented simple view counter of image, with the help of Redis NoSQL database.

### Set-Up Instructions ###

Create a virtual environment to isolate our package dependencies locally, if you are using linux please note that you must specify the version of Python, like that:
 
`$ python3 -m venv venv`

`$ source venv/bin/activate`

`$ pip install -r requirements.txt`

`$ python3 manage.py migrate`

`$ python3 manage.py runserver `

For macOS users:

`$ python -m venv venv`

`$ source venv/bin/activate`

`$ pip install -r requirements.txt`

`$ python manage.py migrate`

`$ python manage.py runserver `

*That's all, you completely installed social website django application.*
