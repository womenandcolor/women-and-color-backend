/**
 * Profile.js
 *
 * @description :: TODO: You might write a short summary of how this model works and what it represents here.
 * @docs        :: http://sailsjs.org/documentation/concepts/models-and-orm/models
 */

module.exports = {

  attributes: {
    firstName: {
      type: 'string',
      required: true
    },
    lastName: {
      type: 'string',
      required: true
    },
    woman: {
      type: 'boolean',
    },
    poc: {
      type: 'boolean',
    },
    pronouns: {
      enum: ['she', 'he', 'they'],
      type: 'string',
    },
    position: {
      type: 'string',
    },
    description: {
      type: 'text'
    },
    company: {
      type: 'string',
    },
    twitter: {
      type: 'string'
    },
    linkedin: {
      type: 'string'
    },
    website: {
      type: 'string'
    },
    user: {
      model: 'user',
      unique: true,
      required: true
    },
    topics: {
      collection: 'topic',
      via: 'profiles',
      dominant: true
    },
    city: {
      model: 'city'
    }
  }
};

