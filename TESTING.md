# Testing

A variety of exploratory tests were performed throughout the project.

## Manual Testing

1. Getting the live deployed site working. This is well documented in the latter sections of [DEPLOYMENT.md](DEPLOYMENT.md)

<details>
<summary>template</summary>
</details>

## Checking server shows homepage

<details>
<summary> # Checking server deploys homepage</summary>

Add the following code to the *home/views.py* file. This tells the server to display "This is the homepage"

![Home/views.py](docs/testing/ca-01-home-views.png)

Add the following code to the *elite_cuisine/urls.py* file.

![Elite_cuisine/urls.py](docs/testing/ca-02-elite-urls.png)

Add the following code to the *elite_cuisine/settings.py* file to installed apps.

![Elite_cuisine/settings.py](docs/testing/ca-03-elite-settings.png)

Use command *python3 manage.py runserver* to check the home app is linked correctly.

![Succesful server](docs/testing/ca-04-succesful-server.png)

</details>

## Creating templates

<details>
<summary> # creating templates</summary>

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

</details>

## superuser 

<details>
<summary> # super user</summary>

When i originally tried to login as a superuser i recieved this error.

![admin error 403](docs/testing/adminlogin-01-error-403.png)

After using code institute support i had forgotten to add.

![CSRF_trusted_Origins](docs/testing/adminlogin-02.png)

Admin login now functions correctly.

![admin access](docs/testing/adminlogin-03.png)

</details>

## CSS and JS

<details>
<summary> # CSS and JS</summary>
</details>

## Registration

<details>
<summary> # Registration</summary>


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

When creating the registration process I had saved the registration.html in the incorrect location. the registration form now appears when /regisitration is appeneded to the servers URL.

![Registration form showing on webpage](docs/testing/registration-02-form-in-url.png)

When checking if the inputs worked. I tried to enter incomplete registrations to see feedback messages. 

### working

- Already taken username

![Username already exists error message](docs/testing/reg-feedback-01-username-taken.png)

- Incorrect email

![email error message](docs/testing/reg-feedback-02-email-incorrect.png)

- Password to similar to name

![password to common error message](docs/testing/reg-feedback-03-password-common.png)

- Passwords dont match 

![Passwords dont match error message](docs/testing/reg-feedback-04-passwords-dont-match.png)

### not working 

- Phone number not numbers 

Using djangos built in validators the phone number now has to be numerical.

![Phone number has to be numbers error message](docs/testing/reg-feedback-05-phone-numbers-validation.png)

- Already taken email

After searching for a solution, comments onforums state that it could be detrimental as hackers can abuse this information if provided to them. Left out for the time being unless there is a safe way.  

### registration/login message

The message to confirm registration was not appearing to adjustments had to be made to the base.html to show the message. 

![Registration message shown on webpage](docs/testing/reg-feedback-06-registration-message.png)

</details>