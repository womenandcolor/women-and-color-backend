/**
 * Policy Mappings
 * (sails.config.policies)
 *
 * Policies are simple functions which run **before** your controllers.
 * You can apply one or more policies to a given controller, or protect
 * its actions individually.
 *
 * Any policy file (e.g. `api/policies/authenticated.js`) can be accessed
 * below by its filename, minus the extension, (e.g. "authenticated")
 *
 * For more information on how policies work, see:
 * http://sailsjs.org/#!/documentation/concepts/Policies
 *
 * For more information on configuring policies, check out:
 * http://sailsjs.org/#!/documentation/reference/sails.config/sails.config.policies.html
 */


module.exports.policies = {

  /***************************************************************************
  *                                                                          *
  * Default policy for all controllers and actions (`true` allows public     *
  * access)                                                                  *
  *                                                                          *
  ***************************************************************************/

  '*': false,
  AuthController: {
    login: true,
    logout: 'isAuthenticated'
  },
  UserController: {
    create: true,
    find: true,
    findOne: true,
    populate: true,
    update: 'isAuthenticated',
    delete: 'isAuthenticated',
    add: 'isAuthenticated',
    remove: 'isAuthenticated',
  },
  ProfileController: {
    find: true,
    findOne: true,
    populate: true,
    create: 'isAuthenticated',
    update: 'isAuthenticated',
    delete: 'isAuthenticated',
    add: 'isAuthenticated',
    remove: 'isAuthenticated',
  },
  CityController: {
    find: true,
    populate: 'isAuthenticated',
    add: 'isAuthenticated',
    remove: 'isAuthenticated',
    update: ['isAuthenticated', 'isAdmin'],
    create: ['isAuthenticated', 'isAdmin'],
    destroy: ['isAuthenticated', 'isAdmin'],
  },
  TopicController: {
    find: true,
    create: 'isAuthenticated',
    populate: 'isAuthenticated',
    add: 'isAuthenticated',
    remove: 'isAuthenticated',
    update: ['isAuthenticated', 'isAdmin'],
    destroy: ['isAuthenticated', 'isAdmin'],
  }
};
