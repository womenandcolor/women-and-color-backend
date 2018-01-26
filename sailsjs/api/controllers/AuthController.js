const passport = require('passport')

module.exports = {
	login: (req, res, next) => {
    passport.authenticate('local', function(err, user, info) {
      if (err) { return next(err); }
      if (!user) { return res.json({ status: 401, message: 'Email or password is incorrect' }); }
      req.logIn(user, function(err) {
        if (err) { return next(err); }
        return res.json({ status: 200, user: req.user })
      });
    })(req, res, next);
  },
  logout: (req, res) => {
    req.logout();
    res.json({ status: 200, message: 'Logged out' });
  }
};

