import cgi, re

def valid_email(email):
  EM_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
  return not email or EM_RE.match(email)

def valid_password(p):
  PW_RE = re.compile(r"^.{3,20}$")
  return p and PW_RE.match(p)

def valid_username(username):
  USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
  return username and USER_RE.match(username)