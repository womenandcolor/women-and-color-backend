/**
 * Bootstrap
 * (sails.config.bootstrap)
 *
 * An asynchronous bootstrap function that runs before your Sails app gets lifted.
 * This gives you an opportunity to set up your data model, run jobs, or perform some special logic.
 *
 * For more information on bootstrapping your app, check out:
 * http://sailsjs.org/#!/documentation/reference/sails.config/sails.config.bootstrap.html
 */

const CITY_OPTIONS = [
  {
    name: 'Toronto',
    province_state: 'Ontario',
    country: 'Canada'
  },
  {
    name: 'Montréal',
    province_state: 'Québec',
    country: 'Canada'
  },
  {
    name: 'Vancouver',
    province_state: 'British Columbia',
    country: 'Canada'
  },
  {
    name: 'Ottawa',
    province_state: 'Ontario',
    country: 'Canada'
  }
]

const TOPIC_OPTIONS = [
  {
    name: 'acquisition'
  },
  {
    name: 'ecommerce'
  },
  {
    name: 'entrepreneurship'
  },
  {
    name: 'product management'
  },
  {
    name: 'user experience'
  },
  {
    name: 'content marketing'
  },
  {
    name: 'copywriting'
  },
  {
    name: 'social media'
  },
  {
    name: 'business development'
  },
  {
    name: 'blogging'
  },
]

function seedCities(callback) {
  City.findOrCreate(CITY_OPTIONS).exec(function(err) {
    if (err) { return callback(err) }
    return callback()
  })
}

function seedTopics(callback) {
  Topic.findOrCreate(TOPIC_OPTIONS).exec(function(err) {
    if (err) { return callback(err) }
    return callback()
  })
}

module.exports.bootstrap = function(cb) {
  async.series([seedCities, seedTopics], cb)
};
