import hmac, re, hashlib, random
from google.appengine.ext import db
from string import letters


#####Security#####

# def create_password(length = 100, characters = (string.punctuation + string.ascii_letters + string.digits)):
#     return ''.join(random.choice(characters) for i in range(length))

secret = '[=||*!G!n+l.@S@0lY7ls?{4"iES~AOdXQB&0$f17lsmz<}:tTg;hkmvDQ}.g_9H"8GI7r_^@A6?}0~jL_ssCX=NpoM?\cMZA6r8'
def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val

## User security ##

def make_salt(length = 5):
    return ''.join(random.choice(letters) for x in range(length))

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)

def valid_pw(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)

def users_key(group = 'default'):
    return db.Key.from_path('users', group)

## Validation ##
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)