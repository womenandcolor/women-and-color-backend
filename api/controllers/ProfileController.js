/**
 * ProfileController
 *
 * @description :: Server-side logic for managing profiles
 * @help        :: See http://sailsjs.org/#!/documentation/concepts/Controllers
 */

module.exports = {
	find: (req, res) => {
    Profile
      .find()
      .populate('topics')
      .exec((err, profiles) => {
      if (err) { return res.badRequest(err) }
      return res.send(profiles)
    })
  }
};

