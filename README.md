# Women and Color

We're building a RESTful API for the Women and Color project, which is a community and database of women and POCs in the tech space.

## Requirements:
- Node
- Express
- Sails.js
- Postgresql

## Get started
- clone the repo: `git clone git@github.com:CivicTechTO/women-and-color-backend.git`
- install packages: `npm install`
- start the server: `sails lift`

## API Documentation

The base url for the API is `/api/v1`.

#### Models

There are currently four models: User, Profile, Topic, and City.

- *User*: `/users`
  - Exclusively for managing the user account and contacting them
  - Fields:
    - `name` (string)
    - `password` (string)

- *Profile* `/profiles`
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
    - `image` (string), ~file upload not implemented yet~
- *City* `/cities`
  - Fields:
    - `name` (string)
    - `province/state` (string)
    - `country` (string)
- *Topic* `/topics`
  - Topics that the speakers are available to speak about
  - Needs to be reorganized into a taxonomy that supports topic categories
  - Fields:
    - `name` (string)
- The User, City, and Topic models are all associated with the Profile.

