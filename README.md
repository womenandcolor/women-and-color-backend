# Women and Color

We're building a RESTful API for the Women and Color project, which is a community and database of women and POCs in the tech space.

## Tech stack:
- Python/Django
- Postgres
- Docker

## Get started
- Copy `env/dev.env.template` as `env/dev.env`
- Install Docker and docker-compose
- Run `docker-compose up`, sometimes the web app comes up before postgres configuration has ended which can cause a failure, if this happens, run `docker-compose up` again.
- Run `docker ps` to get the container ID for the app container (should be the has associated with womenandcolorbackend_app_)
- Open a shell session in the app container: `docker exec -it <container-id> sh`
- Run migrations: `python manage.py migrate`
- Initialize the project: `python manage.py init_project`
- Seed the database with a fake profile: `python manage.py seed_database`
- The server should now be running on `localhost:8000`

### Start the frontend
- Go to the [frontend repo][code-frontend] to clone the repo. Follow the setup instructions there to start the frontend app.

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
    - `image` (string),
    - `page` (string),
    - `location` (foreign key),
    - `display_name` (string),
    - `city` (string),
    - `status` (string),
    - `featured_talks` (array),
    - `topics` (array),
- **Location** `/locations`
  - Fields:
    - `city` (string)
    - `province` (string)
    - `country` (string)
- **Topic** `/topics`
  - Topics that the speakers are available to speak about
  - Needs to be reorganized into a taxonomy that supports topic categories
  - Fields:
    - `topic` (string)
- **Featured Talk** `/featured/talks`
  - Links of past talks uploaded by the user on their profile
  - Fields:
    - `event_name` (string)
    - `talk_title` (string)
    - `url` (string)
    - `profile` (foreign key)
- The User, City, and Topic models are all associated with the Profile.

<!-- Links -->
   [code-frontend]: https://github.com/CivicTechTO/women-and-color-frontend
