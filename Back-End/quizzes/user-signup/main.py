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
		params = {'title': title}
		self.render("user_signup.html", **params)

	def post(self):
		#retrieve information from user
		user = self.request.get('username')
		p1 = self.request.get('password')
		p2 = self.request.get('verify')
		email = self.request.get('email')
		errors = {}

		#these will be preserved if failure
		params = {'username': user,
					'email': email,
					'title': title}
		#validity tests
		if not valid_username(user):
			errors['nameerror'] = "That's not a valid username."
		if valid_password(p1):
			errors['pwerror'] = "That wasn't a valid password."
		if not p1 == p2:
			errors['matcherror'] = "Your passwords don't match."
		if not valid_email(email):
			errors['emailerror'] = "That is not a valid email address."
		
		if not errors:
			self.redirect("/welcome?username=" + user)
		else:
			params = dict(params.items()+errors.items())
			self.render("user_signup.html", **params)

class Welcome(Handler):
	def get(self):
		user = self.request.get('username')
		if valid_username(user):
			self.render('thanks.html', username=user, title=title)
		else:
			self.redirect('/user_signup.html')

app = webapp2.WSGIApplication([('/', MainPage),
							('/welcome', Welcome)],
							debug=True)
