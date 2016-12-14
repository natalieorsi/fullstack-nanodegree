import cgi, re

def valid_email(email):
  if email:
      EM_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
      return EM_RE.match(email)
  return True

def valid_password(p):
  if p:
    PW_RE = re.compile(r"^.{3,20}$")
    return PW_RE.match(p)
  return False

def valid_username(username):
  if username:
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)
  return False