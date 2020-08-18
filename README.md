### social_website_django ###
Pet-project, social website builded with the help of Python, and Django Web framework
This project was implemented with the most required tech stack. Was created a authentication using social Auth (Google/Facebook APIs), activity stream, follow/like system.
Implemented simple view counter of image and ranking bookmarks system, with the help of Redis NoSQL database.

### Set-Up Instructions ###

Create a virtual environment to isolate our package dependencies locally, if you are using linux please note that you must specify the version of Python, like that:
 
`$ python3 -m venv venv`

`$ source venv/bin/activate`

`$ pip install -r requirements.txt`

`$ python3 manage.py migrate`

`$ python3 manage.py runserver `

# For macOS users:

`$ python -m venv venv`

`$ source venv/bin/activate`

`$ pip install -r requirements.txt`

`$ python manage.py migrate`

`$ python manage.py runserver `

# Installing Redis:
If you are using Linux or macOS, download the latest Redis version from https://redis.io/download. Unzip the tar.gz file, enter the redis directory, and compile
Redis using the make command, as follows:

`cd redis-5.0.8
make`

Redis is now installed on your machine. If you are using Windows, the preferred
method to install Redis is to enable the Windows Subsystem for Linux (WSL)
and install it in the Linux system. You can read instructions on enabling WSL and installing Redis at https://redislabs.com/blog/redis-on-windows-10/ .

After installing Redis, use the following shell command to start the Redis server:
src/redis-server

You should see an output that ends with the following lines:

`Server initialized`
`* Ready to accept connections`

By default, Redis runs on port 6379 . You can specify a custom port using the --port flag, for example, redis-server --port 6655. Keep the Redis server running and open another shell. Start the Redis client with the following command:

`src/redis-cli`

You will see the Redis client shell prompt, like this:
`127.0.0.1:6379>`

The Redis client allows you to execute Redis commands directly from the shell

# Using Redis with Python:
It will be installed when you install requirements.txt packages.

*That's all, you completely installed social website django application.*
