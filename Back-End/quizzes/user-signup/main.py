import webapp2, os, jinja2
from forms import valid_email, valid_password

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	title = "Sign up today!"

	def get(self):
		self.render("user_signup.html", title=title)

	def post(self):
		user = self.request.get('username')
		p1 = self.request.get('password')
		p2 = self.request.get('verify')
		em = self.request.get('email')
		if password:
			#why not do a crappy encyption, for fun?
			rot13 = password.encode('rot13')

		self.render("rot13.html", text=rot13, title=title)



app = webapp2.WSGIApplication([('/', MainPage),
							],
							debug=True)
