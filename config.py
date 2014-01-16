from pyramid.config import Configurator
from md5 import md5

log_format = '%(module)s:%(lineno)d %(levelname)s %(message)s'
log_level = 'DEBUG'

http_port = 8880
http_address = '0.0.0.0'

password_salt = md5('firemark to dupa').hexdigest()

config = Configurator()
config.add_static_view('/', 'webapp')
