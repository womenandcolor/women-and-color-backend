var bcrypt = require('bcrypt');
var passport = require('passport');
var LocalStrategy = require('passport-local').Strategy;
// var db = require('../models');

passport.use(new LocalStrategy({ usernameField: 'email', passwordField: 'password' }, (email, password, done) => {
  var user = User.findOne({ email: email }).then(user => {
    if (!user) {
      return done(null, false)
    }

    var hash = user.password;
    bcrypt.compare(password, hash, function(err, res) {
      if (!res) {
        return done(null, false);
      }

      return done(null, user);
    });
  }).catch(err => {
    throw err;
  });
}));

passport.serializeUser(function(user, done) {
  done(null, user.id);
});

passport.deserializeUser(function(id, done) {
  User.findOne({id: id}, function(err, user) {
    done(err, user);
  });
});