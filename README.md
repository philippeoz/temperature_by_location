# Temperature by Location
Simple web application that allows users to view the current temperature at a given
location.

[Aqui temos uma demo. (Temporary)](http://temperature.valfok.com)

This application was developed in Python 3.6, using Django, PostgreSQL, Docker, docker-compose and nginx.

#### How to Setup
Clone:
-  `git clone https://github.com/philippeoz/myprofile.git`

We have two ways to run:
-  With Docker:
    1. [Install Docker](https://docs.docker.com/install/)
    2. [Install docker-compose](https://docs.docker.com/compose/install/)
    3. `cd temperature_by_location` to enter on project dir.
    4. Add a `settings.env` file with some configurations: `DEBUG`, `GOOGLE_API_KEY`, `DARK_SKY_API_KEY`
    5. `docker-compose up --build` or `docker-compose --build -d` (daemon)
- With virtualenv:
    1. [Install Postgresql](https://www.postgresql.org/download/) and create a database (we will call `database`).
    2. [Install Pipenv](https://github.com/pypa/pipenv): `pip install pipenv`
    3. Enter on project dir: `cd temperature_by_location`
    4. `pipenv install`
    5. `cd app`
    6. Inside of 'app' dir, create a `settings.ini` file with some configs:
        ```
        [settings]
        DEBUG=True
        DATABASE_URL=postgres://username:password@host/database
        GOOGLE_API_kEY=faskdjfhaskldfYOURKEYdsjfasfl
        DARK_SKY_API_kEY=faskdjfhaskldfYOURKEYdsjfasfl
        ```
        There are more environment variables that can be configured in `settings.ini`, see in the [settings module](https://github.com/philippeoz/temperature_by_location/tree/master/app/settings).
    7. From here you can choose to enter on virtualenv with `pipenv shell` or run the commands from outside with `pipenv run python`, the example will be outside of env, to do inside just remove the `pipenv run`.
    8. `pipenv run python manage.py migrate`
    9. `pipenv run python manage.py runserver`