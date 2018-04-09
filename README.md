# Women and Color

We're building a RESTful API for the Women and Color project, which is a community and database of women and POCs in the tech space.

## Tech stack:
- Python/Django
- Postgres
- Docker

## Get started
- Copy `env/dev.env.template` as `env/dev.env` and either contact another contributor to get the missing environment variables or provide your own.
- Install Docker and docker-compose
- Run `docker-compose up`, sometimes the web app comes up before postgres configuration has ended which can cause a failure, if this happens, run `docker-compose up` again.
- Run `docker ps` to get the container ID for the app container (should be the has associated with womenandcolorbackend_app_)
- Open a bash session in the app container: `docker exec -it <container-id> bash`
- Run migrations: `python manage.py migrate`
- Seed the database: `python manage.py init_project`
- The server should now be running on `localhost:8000`

### Start the frontend
- You won't see anything on `localhost:8000` until you start the frontend server
- Go to the [frontend repo][code-frontend] to clone the repo. Follow the setup instructions there, then refresh the browser.

## API Documentation

The base url for the API is `/api/v1`.

#### Models

There are currently four models: User, Profile, Topic, and City.

- **User**: `/users`
  - Exclusively for managing the user account and contacting them
  - Fields:
    - `name` (string)
    - `password` (string)

- **Profile** `/profiles`
  - The main representation of speakers.
  - Fields:
    - `firstName` (string)
    - `lastName` (string)
    - `woman` (boolean)
    - `poc` (boolean), short for person of color
    - `pronouns` (string), one of: she, he, they
    - `position` (string)
    - `organization` (string)
    - `description` (string)
    - `twitter` (string)
    - `linkedin` (string)
    - `website` (string)
    - `image` (string), *file upload not implemented yet*
- **City** `/cities`
  - Fields:
    - `name` (string)
    - `province/state` (string)
    - `country` (string)
- **Topic** `/topics`
  - Topics that the speakers are available to speak about
  - Needs to be reorganized into a taxonomy that supports topic categories
  - Fields:
    - `name` (string)
- The User, City, and Topic models are all associated with the Profile.

<!-- Links -->
   [code-frontend]: https://github.com/CivicTechTO/women-and-color-frontend
