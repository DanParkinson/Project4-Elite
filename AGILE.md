# Agile

## Phase 1

- Setup repo
- Create Django project
- Install basic dependencies and add to requirements
- Create procfile to deploy to Heroku
- Create app on Heroku
- Link GitHub repo to Heroku app
- Test to deploy working project ASAP

- Document project creation and deployment
- Perform design thinking exercise for features to include in project
- Add user stories to readme
- Add wireframes to readme
- Identify a colour schema to use in the site
- Mock up initial database design and document in readme
- List and link technologies used in readme

- Learn to use GitHub projects. Create user stories


I would like to deploy to Heroku at this point but My authenticator is not working. So I have decided to begin phase 2 of my planning.

## Phase 2

Focus here is to do with setting up templates to have a view of the home page.

- Setup base.html
- create separate components for site such as head, header, navbar, footer in a subfolder to inject into base.html
- Setup index page in home app
- Build navigation

At this point I was able to deploy to Heroku. I have my templates made for fututre web pages. It is time to build some models. 

## Phase 3

I want to create a way for users to create accounts, login and logout. Django provides a built in users function which I will use. 

- users can register using a form
- when registered users are directed to login page
- users can log in
- home page confirms login 
- users can log out
- when logging out users are redirected to the log in page
- navbar needs editing to include these
- 