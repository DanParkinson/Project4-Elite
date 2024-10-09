# Deployment

It is assumed the user knows how to create a repository on Github.
The linked repo template from the [Code Institute](https://github.com/Code-Institute-Org/gitpod-full-template) was used to start the project.

1. Install Django 4.2.1 with required packages
2. Create a new Django project
3. Create home app
3. Set up project to use PostgreSQL and Cloudinary
4. Deploy project to Heroku

## Install Django 3.2 (LTS) with required packages.

*Django*, a full stack framework will support this project.

To install, type *pip3 install Django~=4.2.1* into the Gitpod terminal.

![Django installed](docs/local_deployment/id-01-install-django.png)

Use command *pip3 freeze --local > requirements.txt* to create requirements.txt and add relavent packages to it. 

## Install gunicorn

To install, type *pip3 install gunicorn~=20.1* into the Gitpod terminal.

Use command *pip3 freeze --local > requirements.txt* to create requirements.txt and add relavent packages to it.


![Gunicorn installed](docs/heroku_deployment/hd-03-gunicorn-install.png)

## Install Whitenoise

To install, type *pip3 install whitenoise~=6.5.0* into the Gitpod terminal.

Use command *pip3 freeze --local > requirements.txt* to create requirements.txt and add relavent packages to it.

![Whitenoise installed](docs/heroku_deployment/hd-09-whitenoise.png)

# Install Psycopg2 and dj-database-url

To install, type *pip3 install dj_database_url~=0.5 psycopg2~=2.9* into the Gitpod terminal.

Use command *pip3 freeze --local > requirements.txt* to create requirements.txt and add relavent packages to it.

![pyscopg2 and dj_databse_url installed](docs/local_deployment/post-01-requirements.png)

# Create Django Project

Using the command *django-admin startproject elite-cuisine* creates our django project.

![elite-cuisine created](docs/local_deployment/cp-01-elite-cuisine-project.png)

Using the command *python3 manage.py runserver* opens the server in port 8000. The server needs allowed hosts in *elite-cuisine/settings.py* to be added.

![Server error message](docs/local_deployment/cp-02-allowed-hosts.png)

Add to allowed hosts in *elite-cuisine/settings.py*

![Allowed hosts added](docs/local_deployment/cp-03-allowed-hosts-added.png)

In the terminal, type *python3 manage.py runserver* to verify local deployment. A message to open a page in the browser pops up using port 8000.

![Successful server response](docs/local_deployment/cp-04-succesful-server.png)

# Create home app

In the terminal, type *python3 manage.py startapp home* to create out homepage app.

![Home app created](docs/local_deployment/ca-01-create-home-app.png)

# Deploy to Heroku 

Navigate to your Heroku dashboard and create a new Heroku app.

![Create Heroku App](docs/heroku_deployment/hd-01-create-app.png)

Add *DISABLE_COLLECTSTATIC* with a Value of 1 to stop Heroku uploading static files.

![Edit Config Vars](docs/heroku_deployment/hd-02-config-vars.png)

Create a Procfile to allow Heroku to deploy using Gunicorn.

![Created Procfile](docs/heroku_deployment/hd-04-procfile.png)

Add Heroku to allowed hosts in elite_cuisine/settings.py.

![Append Heroku to Allowed Hosts](docs/heroku_deployment/hd-05-allowed-hosts.png)

Connect Heroku to your Github account.

![Connect Heroku to Github](docs/heroku_deployment/hd-06-heroku-github.png)

Click deploy branch and wait for completion.

![Deploy Branch](docs/heroku_deployment/hd-07-deploy-branch.png)

Add Eco Dynos.

![Add Eco Dynos](docs/heroku_deployment/hd-08-eco-dynos.png)

# Connect PostgreSQL

Create and env.py file in the top directory and use this code. The postgreSQL code was generated from Code Institute. It has been redacted from the image.

![PostgreSQL code](docs/local_deployment/post-02-env.png)

Use the following code to connect the env.py in the elite_cuisine/settings.py

![env connected](docs/local_deployment/post-03-connect-env.png)

in the elite_cuisine/settings.py file, disconnect the splite database by commenting out the code.

![Splite commented out](docs/local_deployment/post-04-disconnect-splite-database.png)

Use dj-databse-url to connect.

![dj-databse-url connection](docs/local_deployment/post-05-dj-databse-url.png)

# Create superuser

Using the terminal command *python3 manage.py migrate*, create a database.

![First-migration terminal response](docs/local_deployment/post-06-first-migrate.png)

Create a superuser using djangos built in admin and auth apps using temrinal command *python3 manage.py createsuperuser*.

![superuser created](docs/local_deployment/superuser-01.png)

# Connect Heroku to postgreSQL

Deploy a new branch in Heroku.

![Heroku deploy button](docs/local_deployment/post-07-deploy.png)

Create a new convig-var using the name DATABASE-URL and a value of your postgreSQL. This connects Heroku to the postgreSQL.

![Convig-var postgreSQL](docs/local_deployment/post-08-config-vars-postgresql.png)

# Secret Key

Generate a secret key using letters, numbers and symbols that is hard to guess. This is used to keep information private.
Add it to the env.py file with the following code.

![secret key in env](docs/local_deployment/sk-01-env.png)

Update the settings.py file.

![secret key in settings.py](docs/local_deployment/sk-02-settings.png)

Add secret key as a config-var to Heroku. The name should be SECRET_KEY. The value should be your secret key value. 

If done correctly, both local and Heroku deployment should work.

