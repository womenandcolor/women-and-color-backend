module.exports = function(req, res, next) {
 if (req.isAuthenticated()) {
    return next();
  }
  else {
    return res.json({ status: 401, message: 'User is not authenticated' });
  }
};