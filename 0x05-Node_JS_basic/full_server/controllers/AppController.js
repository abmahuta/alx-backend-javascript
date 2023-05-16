/**
 * Contains the miscellaneous route handlers.
 * @author Abdulkadir Badamasi <https://github.com/abmahuta>
 */
class AppController {
  static getHomepage(request, response) {
    response.status(200).send('Hello Holberton School!');
  }
}

export default AppController;
module.exports = AppController;
