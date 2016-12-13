# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2, os, jinja2

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

	def rot13(self, message):
		translated = ""
		message = message[1:len(message)-1]
		for n in message:
			if n.isalpha():
				nord = ord(n)
				nord += 13

				if n.isupper():
					if nord > ord('Z'):
						nord -= 26
					elif nord < ord('A'):
						nord += 26
				elif n.islower():
					if nord > ord('z'):
						nord -= 26
					elif nord < ord('a'):
						nord += 26
				translated += chr(nord)
			else:
				translated += n
		return str(translated[0:len(translated)-1])


class MainPage(Handler):

	def get(self):
		inputs = self.request.get_all("inputs")
		outputs = self.rot13(inputs)
		self.render("rot13.html", inputs=inputs, outputs=outputs, title="ROT13")


app = webapp2.WSGIApplication([('/', MainPage),
							],
							debug=True)
