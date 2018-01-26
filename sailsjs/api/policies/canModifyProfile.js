module.exports = function(req, res, next) {
  User.findOne({id: req.session.passport.user}).populate('profile').exec((err, user) => {
    if (user.profile[0].id == req.param('id') || user.isAdmin) {
      return next()
    } else {
      return res.json({ status: 401, message: 'This action is not authorized' });
    }
  })
};