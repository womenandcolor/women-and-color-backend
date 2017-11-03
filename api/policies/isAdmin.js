module.exports = function(req, res, next) {
 if (req.session.user.isAdmin) {
    return next();
  }
  else {
    return res.json({ status: 401, message: 'User does not have Admin privileges' });
  }
};