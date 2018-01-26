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
  },
  search: (req, res) => {
    let searchQuery = {};
    let topicsIds = [];

    if (req.query.woman === 'true') {
      searchQuery.woman = true;
    }

    if (req.query.poc === 'true') {
      searchQuery.poc = true;
    }

    if (!!req.query.city) {
      searchQuery.city = parseInt(req.query.city);
    }

    if (!!req.query.topics) {
      const topicsArray = decodeURI(req.query.topics).split(',');
      Topic.find({ name: topicsArray }).exec((err, topics) => {
        topicsIds = topics.map((topic) => (topic.id));
      })
    }

    Profile.find(searchQuery).populate('topics').exec((err, results) => {
      if (err) { return res.serverError(err) }

      if (!!req.query.topics) {
        const filteredResults = results.filter((profile) => {
          const profileTopicIds = profile.topics.map((topic) => (topic.id))
          const intersection = _.intersection(profileTopicIds, topicsIds)
          return intersection.length > 0
        })

        return res.send(filteredResults)
      }

      return res.send(results)
    })
  }
};

