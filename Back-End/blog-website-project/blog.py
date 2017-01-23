import os, random, hashlib, webapp2, jinja2
from google.appengine.ext import db
from string import letters
from convenience import render_str
from secure import make_secure_val, check_secure_val, valid_username, valid_password, valid_email
from users import User
from post import Post
from comments import Comment
from likes import Like

#####Blog Handler#####

class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        """
            Write output to browser.
        """
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        """
            Render HTML string.
        """
        params['user'] = self.user
        return render_str(template, **params)

    def render(self, template, **kw):
        """
            Renders HTML using Jinja, based on template.
        """
        self.write(self.render_str(template, **kw))

    def set_cookie(self, name, val):
        """
            Sends new cookie to browser.
        """
        cookiev = make_secure_val(val)
        self.response.headers.add_header('Set-Cookie',
            '%s=%s; Path=/' % (name, cookiev))

    def read_cookie(self, name):
        """
            Reads stored cookie from browser.
        """
        cookiev = self.request.cookies.get(name)
        return cookiev and check_secure_val(cookiev)

    def login(self, user):
        """
           Activates cookie storage for verified user. 
        """
        self.set_cookie('user_id', str(user.key().id()))

    def logout(self):
        """
            Removes user login cookie from client browser.
        """
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def initialize(self, *a, **kw):
        """
            Spez's fix for ensuring cookie is stored in user object on page render.
        """
        webapp2.RequestHandler.initialize(self, *a, **kw)
        userid = self.read_cookie('user_id')
        self.user = userid and User.by_id(int(userid))

def render_post(response, post):
    """
       Renders post data. 
    """
    response.out.write(post.subject)
    response.out.write(post.content)

##### Blog Posts #####

def blog_key(name = 'default'):
    """
        Store blog key information.
    """
    return db.Key.from_path('blogs', name)

#Front page handler
class Front(BlogHandler):
    def get(self):
        """
            Renders home page with posts sorted by date descending.
        """
        posts = Post.all().order('-created')
        self.render('front.html', posts = posts)

#Blog post page handler
class PostPage(BlogHandler):
    def get(self, post_id):
        """
           Renders post page with all content, including comments and likes.
        """
        post = db.get(db.Key.from_path('Post', int(post_id), parent=blog_key()))
        if not post: #Avoid app errors by using browser 404 error
            self.error(404)
            return

        all_comments = db.GqlQuery("select * from Comment where parent_post = " + post_id + "order by created desc")

        all_likes =  db.GqlQuery("select * from Like where parent_post = " + post_id)

        num_likes = all_likes.count()

        self.render("permalink.html", post = post, comments = all_comments, num_likes = num_likes, post_id = post_id)

    def post(self, post_id):
        post = db.get(db.Key.from_path('Post', int(post_id), parent=blog_key()))
        #print "post_id:",post_id
        all_comments = db.GqlQuery("SELECT * FROM Comment WHERE parent_post = " + post_id + "order by created desc")
        all_likes =  db.GqlQuery("SELECT * FROM Like WHERE parent_post = " + post_id)

        if not post:
            self.error(404)
            return

        """
            On posting comment, new comment tuple is created and stored,
            with relationship data of user and post.
        """
        if(self.user):
            if(self.request.get('comment')): #Create comment tuple
                cmt = Comment(parent = blog_key(), author = self.user.key().id(),
                            comment = self.request.get('comment'), parent_post = int(post_id))
                cmt.put()
                self.redirect('/blog/%s' % post_id)

            if(self.request.get('like') and (self.request.get('like') == "true")): #Create Like object
                liker = self.user.key().id()
                liked_by_all = db.GqlQuery("SELECT DISTINCT liked_by FROM Like WHERE parent_post = " + post_id)
                liked_list = liked_by_all.fetch(limit=10000)
                likes_list = str([x.liked_by for x in liked_list])
                previous_like = str(liker) in likes_list

                if liker == post.author:
                    error_msg = "It goes without saying that you like your own post."
                    num_likes = all_likes.count()
                    self.render("permalink.html", post = post, comments = all_comments, error = error_msg, num_likes = num_likes, post_id = post_id)
                    return

                elif not previous_like:
                    new_like = Like(parent=blog_key(), liked_by = self.user.key().id(), parent_post = int(post_id))
                    new_like.put()

                else:
                    error_msg = "You already liked this post."
                    num_likes = all_likes.count()
                    self.render("permalink.html", post = post, comments = all_comments, error = error_msg, num_likes = num_likes, post_id = post_id)
                    return

        else:
            self.render("login-form.html", error = "You need to be logged in to like posts or submit comments.")
            #return

        self.redirect('/blog/%s' % post_id)

#Post submission page
class NewPost(BlogHandler):
    def get(self):
        """
           Renders post submission page only if user is logged in. 
        """
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        """
           Submits post if all forms are complete. 
        """
        if not self.user:
            self.redirect('/blog') #no anonymous posts allowed!

        subject = self.request.get('subject')
        content = self.request.get('content')
        author = self.user.key().id()

        if subject and content:
            curr_post = Post(parent = blog_key(), subject = subject, content = content, author = author)
            curr_post.put()
            self.redirect('/blog/%s' % str(curr_post.key().id()))
        else:
            error = "Please finish writing your title and text."
            self.render("newpost.html", subject = subject, content = content, error = error)

#Post edit page
class EditPost(BlogHandler):
    def get(self, post_id):
        """
            Verifies user and renders post edit page.
        """
        if self.user:
            post = db.get(db.Key.from_path("Post", int(post_id), parent = blog_key()))

            if post.author == self.user.key().id():
                self.render("editpost.html", subject = post.subject, content = post.content)
            else:
                all_comments = db.GqlQuery("select * from Comment where parent_post = " + post_id + "order by created desc")
                all_likes =  db.GqlQuery("SELECT * FROM Like WHERE parent_post = " + post_id)

                self.render("permalink.html", post = post, comments = all_comments, num_likes = all_likes.count(), error = "You didn't make this post, so you can't edit it.")

                #self.redirect("/blog/" + post_id + "?error=access-denied")

        else:
            self.render("login-form.html", error = "You must log in to edit your posts.")

    def post(self, post_id):
        """
            Changes post information.
        """
        if not self.user:
            self.redirect('/blog')

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            post = db.get(db.Key.from_path('Post', int(post_id), parent = blog_key()))
            post.subject = subject
            post.content = content
            post.put()
            self.redirect('/blog/%s' % post_id)
        else:
            error = "Please don't leave any field blank."
            self.render("editpost.html", subject=subject,
                        content=content, error=error)

#Delete posts
class DeletePost(BlogHandler):
    def get(self, post_id):
        post = db.get(db.Key.from_path('Post', int(post_id), parent = blog_key()))
        if self.user:
            if post.author == self.user.key().id():
                post.delete()
                self.redirect("/blog/")

            else:
                all_comments = db.GqlQuery("select * from Comment where parent_post = " + post_id + "order by created desc")
                all_likes =  db.GqlQuery("SELECT * FROM Like WHERE parent_post = " + post_id)

                self.render("permalink.html", post = post, comments = all_comments, num_likes = all_likes.count(), error="You didn't make this post, so you can't delete it.")

        else:
            self.render("permalink.html", post = post, error="You are not logged in, so you cannot delete posts.")

#Edit comments
class EditComment(BlogHandler):
    def get(self, post_id, comment_id):
        """
            Retrieves comment edit page.
        """
        all_comments = db.GqlQuery("select * from Comment where parent_post = " + post_id + "order by created desc")
        all_likes =  db.GqlQuery("SELECT * FROM Like WHERE parent_post = " + post_id)
        post = db.get(db.Key.from_path('Post', int(post_id), parent=blog_key()))

        if self.user:
            comment = db.get(db.Key.from_path('Comment', int(comment_id), parent=blog_key()))

            if comment.author == self.user.key().id():
                self.render("editcomments.html", comment=comment.comment)
            else:
                self.render("permalink.html", post = post, comments = all_comments, num_likes = all_likes.count(), error="You didn't write this comment, so you can't edit it.")
        else:
            self.render("permalink.html", post = post, comments = all_comments, num_likes = all_likes.count(), error="You need to be logged in to edit comments.")

    def post(self, post_id, comment_id):
        """
            Updates comment post.
        """
        post = db.get(db.Key.from_path('Post', int(post_id), parent=blog_key()))
        all_comments = db.GqlQuery("select * from Comment where parent_post = " + post_id + "order by created desc")
        all_likes =  db.GqlQuery("SELECT * FROM Like WHERE parent_post = " + post_id)

        if not self.user:

            self.render("permalink.html", post = post, comments = all_comments, num_likes = all_likes.count(), error = "You need to be logged in to edit comments.")

        all_comments = self.request.get('comment')

        if all_comments:
            cmt = db.get(db.Key.from_path('Comment', int(comment_id), parent = blog_key()))
            cmt.comment = self.request.get('comment')
            cmt.put()

            self.redirect('/blog/%s' % post_id)
            #self.render("permalink.html", post = post, comments = all_comments, num_likes = all_likes.count())

        else:
            error = "Please don't leave any fields blank."
            self.render("editcomments.html", post_id = post_id, comments = all_comments, error = error)

#Dekete comments
class DeleteComment(BlogHandler):

    def get(self, post_id, comment_id):
        all_comments = db.GqlQuery("select * from Comment where parent_post = " + post_id + "order by created desc")
        post = db.get(db.Key.from_path('Post', int(post_id), parent = blog_key()))
        all_likes =  db.GqlQuery("SELECT * FROM Like WHERE parent_post = " + post_id)

        if self.user:
            cmt = db.get(db.Key.from_path('Comment', int(comment_id), parent=blog_key()))
            if cmt.author == self.user.key().id():
                cmt.delete()
                self.render("permalink.html", post = post, comments = all_comments, num_likes = all_likes.count(), success = "Comment successfully deleted")
            else:
                self.render("permalink.html", post = post, comments = all_comments, num_likes = all_likes.count(), error = "You didn't write this comment, so you can't delete it.")
        else:
            self.render("permalink.html", post = post, comments = all_comments, num_likes = all_likes.count(), error = "You need to be logged in to delete comments.")

    # def post(self, post_id, comment_id):
    #     EditComment.post(self, post_id, comment_id)

#User registration handler
class Register(BlogHandler):
    def get(self):
        """
           Renders registration page. 
        """
        self.render("signup-form.html")

    def post(self):
        """
           Verifies correct registration criteria and submits new user. 
        """
        have_error = False
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')

        params = dict(username = self.username,
                      email = self.email)

        if not valid_username(self.username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(self.password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif self.password != self.verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(self.email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.render('signup-form.html', **params)
        else:
            self.done()

    def done(self):
        u = User.by_name(self.username)
        """
           Make sure the user doesn't already exist. 
        """
        if u:
            msg = 'Sorry, that username is taken.'
            self.render('signup-form.html', error_username = msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect('/blog')    

class Login(BlogHandler):
    def get(self):
        """
           Render login form. 
        """
        self.render('login-form.html')

    def post(self):
        """
           Logs user in. 
        """
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/blog')
        else:
            msg = 'Invalid login'
            self.render('login-form.html', error = msg)

class Logout(BlogHandler):
    def get(self):
        """
           Logs user out.
        """
        self.logout()
        self.redirect('/blog')

app = webapp2.WSGIApplication([('/', Front),
                               ('/blog/?', Front),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/blog/([0-9]+)/edit', EditPost),
                               ('/blog/([0-9]+)/delete', DeletePost),
                               ('/blog/([0-9]+)/([0-9]+)/edit', EditComment),
                               ('/blog/([0-9]+)/([0-9]+)/delete', DeleteComment),
                               ],
                              debug=True)
