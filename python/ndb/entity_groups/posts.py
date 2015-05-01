from google.appengine.ext import ndb
import datetime

class Post(ndb.Model):
    content = ndb.TextProperty()
    posted = ndb.DateTimeProperty(auto_now_add=True)

def make_post(user_id, post_text):
    """ put a post made by the given user, with the given test in datastore"""
    post = Post(key=ndb.Key('User', user_id, 'Post'), 
            content = post_text)
    post.put()

def get_posts(user_id=None, since=datetime.min):
    """ Retrieve all posts since specified date time. If user_id is specified,
    retrieves only posts by that user, in a strongly consistent manner """
    if user_id is None:
        """ eventually consistent """
        return Account.query(Account.posted >= since).order(-Account.posted)
    else:
        """ strongly consistent """
        return Account.query(
                parent = ndb.Key('User', user_id),
                Account.posted >= since).order(-Account.posted)
