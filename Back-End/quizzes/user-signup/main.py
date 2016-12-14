import webapp2, os, jinja2
from forms import valid_email, valid_password, valid_username

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)

title = "Sign up today!"

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):

	def get(self):
		self.render("user_signup.html", title=title)

	def post(self):
		user = self.request.get('username')
		p1 = self.request.get('password')
		p2 = self.request.get('verify')
		email = self.request.get('email')
		nameerror, pwerror, matcherror, emailerror = ""
		if not valid_username(user):
			nameerror = "That's not a valid username."
		if not valid_password(p1):
			pwerror = "That wasn't a valid password."
		if not p1 == p2:
			matcherror = "Your passwords don't match."
		if not valid_email(email):
			emailerror = "That is not a valid email address."
		elif not (nameerror or pwerror or matcherror or emailerror):
			self.render("thanks.html", title="Thanks!", user=user)
		else:
			self.render("user_signup.html", text=rot13, title=title)



app = webapp2.WSGIApplication([('/', MainPage),
							],
							debug=True)
