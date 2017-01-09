from google.appengine.ext import db
from user import User


class Like(db.Model):
    liked_by = db.IntegerProperty(required=True)
    parent_post = db.IntegerProperty(required=True)

    def retrieveUser(self):
        user_obj = User.by_id(self.liked_by)
        return user_obj.name