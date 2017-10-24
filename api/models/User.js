const bcrypt = require('bcrypt')
const saltRounds = 10;

module.exports = {
  attributes: {
    email: {
      type: 'string',
      unique: true,
      email: true
    },
    password: {
      type: 'string',
      minLength: 6,
      required: true
    },
    profile: {
      collection: 'profile',
      via: 'user'
    },
    city: {
      model: 'city'
    }
  },
  beforeCreate: (user, next) => {
    bcrypt.hash(user.password, saltRounds, (err, hash) => {
      if (err) {
        next(err)
      } else {
        user.password = hash;
        next();
      }
  });
  }
};

