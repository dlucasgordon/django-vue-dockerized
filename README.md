<a href="https://github.com/vchaptsev/cookiecutter-django-vue">
    <img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg" />
</a>


codecovify
==========

This is a template app that contains the following:
- Backend: A dockerized Django app that connects to a Postgres database. This app contains simple views for User management (Login/ Logout/ Register). All those functions are powered through an API that is built with DjnagoRestFramework (https://www.django-rest-framework.org/#example)

- Frontend: A dockerized VueJS app that interacts with the Backend. On the home page, the app loads a simple VueJS component that calls the ackend's /api/users API and to list the registered users in the database.



## Development
To start the server, run:
+  `docker-compose up --build`


## Todos
- Send verbose column names to display on frontend

- Loading commits directly from the table vs first fetching from the SVC apis is a little clunky. The `reload` parameter, which tells the Django api endpoint to reload from the Bitbucket/Github apis, could be abused. Ideally the Django api endpoint accessed from Vue would only fetch from the table directly, and then we'd have some other process running in the backend to periodically update the commit data to the tables, ie once per minute.

- When loading commits from the Bitbucket/Github apis, we should check by date and only grab the new commits since the last update. Also we need to deal with pagination, currently only the first pages are fetched.

- Refactor the vue commit tables and relevant logic to be generated from one component (DRY).

- Refactor Bitbucket and Github views to DRY, and extract api logic out of view classes.

- Move constants in views to settings, and change URIs and endpoints to take arbitrary usernames and repos.

- Frontend table formatting should be improved.

- Started working on author filtering, unfinished