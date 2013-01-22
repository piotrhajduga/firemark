from md5 import md5

log_format = '%(asctime)s %(levelname)7s [%(module)s %(lineno)d %(funcName)s] %(message)s'
log_level = 'DEBUG'
http_port = 8880

db_url = '%s://%s:%s@%s/%s' % (
            'mysql',                      # dialect
            'firemark',                   # user
            'dupa', # password
            'localhost',                  # host
            'firemark'                    # database
        )
db_encoding = 'utf-8'
db_echo = False

password_salt = md5('firemark to dupa').hexdigest()
