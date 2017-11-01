# Women and Color

We're building a RESTful API for the Women and Color project, which provides conference organizers with a database of potential speakers that identify as women and/or people of color.

### Tech:
- Node.js
- Express
- Sqlite

### Get started
- pull the repo
- install packages: `npm install`
- install sequelize-cli and nodemon globally: `npm install -g sequelize-cli nodemon`
- run database migrations: `sequelize db:migrate`
- start the server locally: `DEBUG=women-and-color:* npm run devstart`