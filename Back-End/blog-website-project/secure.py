import hmac
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