FROM node:9.3.0
MAINTAINER Mark Gituma <mark.gituma@gmail.com>

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT
COPY package.json package.json
RUN npm install
COPY . .
EXPOSE 1337
CMD [ "npm", "start" ]
