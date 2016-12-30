import os, re, random, hashlib, hmac, webapp2, jinja2
from google.appengine.ext import db
from string import letters
from convenience import render_str
from secure import check_secure_val
from users import User
from post import Post

#####Blog Handler#####

class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        params['user'] = self.user
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_cookie(self, name, val):
        cookiev = make_secure_val(val)
        self.response.headers.add_header('Set-Cookie',
            '%s=%s; Path=/' % (name, cookiev))

    def read_cookie(self, name):
        cookiev = self.request.cookies.get(name)
        return cookiev and check_secure_val(cookiev)

    def login(self, user):
        self.set_cookie('user_id', str(user.key().id()))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def initialize(self, *a, **kw): #Spez's fix for ensuring cookie is stored in user object
        webapp2.RequestHandler.initialize(self, *a, **kw)
        userid = self.read_cookie('user_id')
        self.user = userid and User.by_id(int(userid))

def render_post(response, post):
    response.out.write(post.subject)
    response.out.write(post.content)



##### Blog Posts #####

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

#Front page handler
class Front(BlogHandler):
    def get(self):
        posts = greetings = Post.all().order('-created')
        self.render('front.html', posts = posts)

#Blog post page handler
class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post: #Avoid app errors by using browser 404 error
            self.error(404)
            return

        self.render("permalink.html", post = post)

#Post submission page
class NewPost(BlogHandler):
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            self.redirect('/blog') #no anonymous posts allowed!

        subject = self.request.get('subject')
        content = self.request.get('content')
        author = self.request.get(self.user)

        if subject and content:
            curr_post = Post(parent = blog_key(), subject = subject, content = content)
            curr_post.put()
            self.redirect('/blog/%s' % str(curr_post.key().id()))
        else:
            error = "Please finish writing your title and text."
            self.render("newpost.html", subject=subject, content=content, error=error)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class Register(BlogHandler):
    def get(self):
        self.render("signup-form.html")

    def post(self):
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
        #make sure the user doesn't already exist
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
        self.render('login-form.html')

    def post(self):
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
        self.logout()
        self.redirect('/blog')

app = webapp2.WSGIApplication([('/', Front),
                               ('/blog/?', Front),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ],
                              debug=True)
