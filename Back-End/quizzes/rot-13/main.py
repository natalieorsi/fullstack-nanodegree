import webapp2, os, jinja2, sys

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

	def get(self):
		self.render("rot13.html", title="ROT13")

	def post(self):
		rot13 = ''
		text = self.request.get('text')
		if text:
			rot13 = text.encode('rot13')

		self.render("rot13.html", text=rot13, title="ROT13")

app = webapp2.WSGIApplication([('/', MainPage),
							],
							debug=True)
