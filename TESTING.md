# Testing

A variety of exploratory tests were performed throughout the project.

## Manual Testing

1. Getting the live deployed site working. This is well documented in the latter sections of [DEPLOYMENT.md](DEPLOYMENT.md)

2. Checking the deployed site opens on the homepage.
- create a function based view in home
- create a path in the url file in the home app
- reference the home app url in the main project url file

Add the following code to the *home/views.py* file. This tells the server to display "This is the homepage"

![Home/views.py](docs/testing/ca-01-home-views.png)

Add the following code to the *elite_cuisine/urls.py* file.

![Elite_cuisine/urls.py](docs/testing/ca-02-elite-urls.png)

Add the following code to the *elite_cuisine/settings.py* file to installed apps.

![Elite_cuisine/settings.py](docs/testing/ca-03-elite-settings.png)

Use command *python3 manage.py runserver* to check the home app is linked correctly.

![Succesful server](docs/testing/ca-04-succesful-server.png)

### Creating templates

Update the *home/views.py* file.

![Updated home/views.py](docs/testing/temp-01-home-views.png)

Create and update the *home/urls.py* file.

![Updated home/urls.py](docs/testing/temp-02-home-urls.png)

Update the *elite_cuisine/urls.py* file.

![Updated elite_cuisine/urls.py](docs/testing/temp-03-elite-cuisine-urls.png)

Run server using command *python3 manage.py runserver* to view that urls route is correct. Error syaing *templates does not exist* shows route is correct.

![templates does not exist error message in server](docs/testing/temp-04-template-dosent-exist.png)

elite_cuisine/settings.py needs updatinf with templates DIR.

![templates dir](docs/testing/temp-05-templates_dir.png)

![templates route](docs/testing/temp-06-templates-route.png)

After creating the base.html, partial htmls and index.html in the templates directory. The server now responds with index.html. 

![templates directory](docs/testing/temp-07-templates.png)

![Server showing index.html](docs/testing/temp-08-basehtml-works.png)

### superuser 

When i originally tried to login as a superuser i recieved this error.

![admin error 403](docs/testing/adminlogin-01-error-403.png)

After using code institute support i had forgotten to add.

![CSRF_trusted_Origins](docs/testing/adminlogin-02.png)

Admin login now functions correctly.

![admin access](docs/testing/adminlogin-03.png)

### CSS and JS

### Django auth function 

Django includes a built in authentication system to register, login and log out of accounts. In *elite_cuisine/urls.py* add the url link to load auth package.

'''

path('accounts/', include('django.contrib.auth.urls')), #Authentication URLS

'''

Appending */accounts/login* or */accounts/logout* to the server URL should load a page. 

*/accounts/login* gives an error saying no template present. Thats because it needs to be created.

![login message](docs/testing/auth-01-login-error.png)

*/accounts/logout* provides this:

![logout message](docs/testing/auth-02-logout.png)

Now that they load I need to create a registration from for users to log into

