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

# Create Django Project

Using the command *django-admin startproject elite-cuisine* creates our django project

![elite-cuisine created](docs/local_deployment/cp-01-elite-cuisine-project.png)

Using the command *python3 manage.py runserver* opens the server in port 8000. The server needs allowed hosts in *elite-cuisine/settings.py* to be added.

![Server error message](docs/local_deployment/cp-02-allowed-hosts.png)

Add to allowed hosts in *elite-cuisine/settings.py*

![Allowed hosts added](docs/local_deployment/cp-03-allowed-hosts-added.png)

In the terminal, type *python3 manage.py runserver* to verify local deployment. A message to open a page in the browser pops up using port 8000.

![Allowed hosts added](docs/local_deployment/cp-04-succesful-server.png)


