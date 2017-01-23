from google.appengine.ext import db
from users import User

#Comment class
class Comment(db.Model):
    comment = db.TextProperty(required=True)
    parent_post = db.IntegerProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    author = db.IntegerProperty(required=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    def retrieveUser(self):
        user_obj = User.by_id(self.author)
        return user_obj.name