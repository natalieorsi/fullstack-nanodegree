import cgi, re

def valid_email(email):
  if email and (email contains '.') and (len(email)>4):
      return True
  return False

def valid_password(p1,p2):
  if (p1 and p2) and (p1 == p2):
      return True
  return False

def valid_username(username):
  if username:
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)
  return False